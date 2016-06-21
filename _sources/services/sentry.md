---
title: Sentry
sorting: A
---

How to setup Sentry server?
===========================

The instruction is tested under **Ubuntu 14.04 LTS**.

Login under `sentry` user with sudo rights.

Then set up server locales to use UTF-8:

```bash
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8
```

**Check your current locale with `locale` command!** If it's not UTF-8, try re-login.

1. Add extra repositories:

    ```bash
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:chris-lea/redis-server
    ```

2. Install Redis and PostgreSQL:

    ```bash
sudo apt-get install -y redis-server
sudo apt-get install -y postgresql-client postgresql-9.3 postgresql-server-dev-9.3 postgresql-common postgresql-contrib
    ```

3. Install required packages:

    ```bash
sudo apt-get install -y python-setuptools python-pip python-dev libxslt1-dev gcc libffi-dev libjpeg-dev libxml2-dev libxslt-dev libyaml-dev python-virtualenv
    ```

4. Install Nginx

    ```bash
sudo apt-get remove -y apache2
sudo apt-get install -y nginx-full
    ```

5. Install and activate Virtualenv:

    ```bash
mkdir -p ~/env && virtualenv ~/env/sentry
source ~/env/sentry/bin/activate
    ```

6. Install Sentry

    ```bash
pip install sentry
    ```

7. Init Sentry config

    ```bash
mkdir -p ~/etc/sentry && sentry init ~/etc/sentry
    ```

8. Setup database

    ```bash
echo -n "New database user password: " && read -s PASSWORD && echo &&\
sudo -u postgres createuser -dRS sentry &&\
sudo -u postgres psql -c "ALTER ROLE sentry WITH PASSWORD '$PASSWORD';" &&\
echo "127.0.0.1:*:sentry:sentry:${PASSWORD}" > ~/.pgpass && echo &&\
chmod 600 ~/.pgpass &&\
createdb -E utf-8 sentry
    ```

9. Update Sentry config

    ```bash
vi ~/etc/sentry/sentry.conf.py
    ```

    database config:

    ```python
DATABASES = {
    'default': {
        'ENGINE': 'sentry.db.postgres',
        'NAME': 'sentry',
        'USER': 'sentry',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
    ```

    queue config:

    ```python
    BROKER_URL = 'redis://127.0.0.1:6379/0'
    ```

    host config:

    ```python
    SENTRY_WEB_HOST = '127.0.0.1'
    ```

    disable sign ups:

    ```python
# Disable registrations
SENTRY_FEATURES = {
    'auth:register': False,
    'social-auth:register': False,
}
    ```

10. Run Sentry database migrations and create admin user:

    ```bash
SENTRY_CONF=$HOME/etc/sentry sentry upgrade
SENTRY_CONF=$HOME/etc/sentry sentry createuser
    ```

11. Setup Nginx web proxy, no SSL

    Paste config to `~/etc/nginx/sentry`:

    ```nginx
    server {
        listen 80;
        server_name sentry.MYSITE.com;

        root /home/sentry/www;

        location ~ ^/(\.well-known)/ {
            root /home/sentry/www;
        }

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://127.0.0.1:9000;
        }
    }    
    ```

    test config and restart:

    ```bash
sudo ln -s /home/sentry/etc/nginx/sentry /etc/nginx/sites-enabled/sentry
sudo nginx -t
sudo service nginx restart
    ```

12. Install LetsEncrypt certificate

    ```bash
mkdir src && git clone https://github.com/letsencrypt/letsencrypt src/letsencrypt
cd src/letsencrypt && ./letsencrypt-auto --help
mkdir -p /home/sentry/www
./letsencrypt-auto certonly --webroot -w /home/sentry/www -d sentry.MYSITE.com
    ```

13. Setup Nginx web proxy, with SSL

    Paste config to `~/etc/nginx/sentry`:

    ```nginx
    server {
        listen 80;
        server_name sentry.MYSITE.com;
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name sentry.MYSITE.com;
        client_max_body_size 4m;

        ssl_certificate /etc/letsencrypt/live/sentry.MYSITE.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/sentry.MYSITE.com/privkey.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

        root /home/sentry/www;

        location ~ ^/(\.well-known)/ {
            root /home/sentry/www;
        }

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://127.0.0.1:9000;
        }
    }
    ```

    then test config and restart:

    ```bash
    sudo nginx -t
    sudo service nginx restart
    ```

14. Add UpStart scripts for main app

    Add config with `sudo vi /etc/init/sentry.conf`:

    ```bash
    description "Sentry web application"
    start on runlevel [2345]
    stop on runlevel [016]
    respawn

    setuid sentry
    setgid sentry

    env LANG=en_US.UTF-8
    env SENTRY_CONF=/home/sentry/etc/sentry

    script
        exec /home/sentry/env/sentry/bin/sentry run web
    end script
    ```

    start the service:

    ```bash
    sudo service sentry start
    ```

15. Add UpStart scripts for worker

    Add config with `sudo vi /etc/init/sentry-worker.conf`:

    ```bash
    description "Sentry workers"
    start on runlevel [2345]
    stop on runlevel [016]
    respawn

    setuid sentry
    setgid sentry

    env LANG=en_US.UTF-8
    env SENTRY_CONF=/home/sentry/etc/sentry

    script
        exec /home/sentry/env/sentry/bin/sentry run worker
    end script
    ```

    start the worker:

    ```bash
    sudo service sentry-worker start
    ```

16. Add UpStart scripts for cron

    Add config with `sudo vi /etc/init/sentry-cron.conf`:

    ```bash
    description "Sentry cron"
    start on runlevel [2345]
    stop on runlevel [016]
    respawn

    setuid sentry
    setgid sentry

    env LANG=en_US.UTF-8
    env SENTRY_CONF=/home/sentry/etc/sentry

    script
        exec /home/sentry/env/sentry/bin/sentry run cron
    end script
    ```

    start the Sentry cron:

    ```bash
    sudo service sentry-cron start
    ```


### Related articles

- https://docs.getsentry.com/on-premise/server/installation/

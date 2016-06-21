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

...

### Related articles

- https://docs.getsentry.com/on-premise/server/installation/

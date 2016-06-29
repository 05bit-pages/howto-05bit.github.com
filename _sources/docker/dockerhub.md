How to run DockerHub on start?
==============================

Create the DockerHub start script with `sudo vi /usr/local/bin/docker-hub-start`:

```bash
#!/bin/sh
IP_ADDR=`/usr/bin/dig +short f7458dd3-64ea-47b4-833c-8d340b12637d.priv.cloud.scaleway.com`
/usr/bin/docker run --rm -p ${IP_ADDR}:5000:5000 --name registry registry:2
```

Set exec permissions to the script:

```bash
sudo chmod +x /usr/local/bin/docker-hub-start
```

Create DockerHub systemd service definition to with `sudo vi /etc/systemd/system/docker-hub.service`:

```ini
[Unit]
Description=DockerHub service
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/local/bin/docker-hub-start
ExecStop=/usr/bin/docker stop -t 2 registry

[Install]
WantedBy=default.target
```

Run the service:

```bash
sudo systemctl start docker-hub
```

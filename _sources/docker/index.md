---
title: Docker
---

Docker Tips
===========

### How to remove untagged images?

```bash
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

Read more:

- http://stackoverflow.com/questions/32723111/how-to-remove-old-and-unused-docker-images

### How to use Docker without sudo?

Add the connected user "${USER}" to the docker group. Change the user name to match your preferred user:

```bash
sudo gpasswd -a ${USER} docker
```

Restart the Docker daemon:

```bash
sudo service docker restart
```

Read more:

- http://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo

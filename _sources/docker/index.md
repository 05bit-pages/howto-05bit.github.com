---
title: Docker
---

Docker Tips
===========

### How to remove untagged images?

```bash
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

### Related links

 - http://stackoverflow.com/questions/32723111/how-to-remove-old-and-unused-docker-images
---
title: Shell Tips
sorting: A
---

Shell Tips
==========

### How to remove all files matching pattern recursively?

```bash
find . -name "*.pyc" -delete
```

or

```bash
find . -name "*.pyc" -exec rm -f {} \;
```bash

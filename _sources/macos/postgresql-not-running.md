---
title: PostgreSQL is not running
---

PostgreSQL is not running
=========================

PostgreSQL is installed but not running. How to start it?

First, just try:

```bash
brew services start postgresql
```

If it doesn't help, the most probably reason in present `postmaster.pid` file, just remove it:

```bash
rm /usr/local/var/postgres/postmaster.pid
```

### Related articles

- https://coderwall.com/p/zf-fww/postgres-on-osx-with-homebrew-not-running-after-osx-crash
- https://keita.blog/2016/01/09/homebrew-and-postgresql-9-5/

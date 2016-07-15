---
title: PostgreSQL
sorting: P
---

PostgreSQL Tips
===============

How to set password for user?
-----------------------------

```
psql -c '\password' postgres
```

Enter the new password here.

Add that password to `~/.pgpass`:

```bash
cat > ~/.pgpass && chmod 600 ~/.pgpass
```

paste the line replacing `<user>` and `<password>` values:

```
127.0.0.1:*:*:<user>:<password>
```

(^D for save)

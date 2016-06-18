---
title: sudoers
---

How to add a user to sudoers?
=============================

You will probably need to add user to sudoers so they could run commands via `sudo`.

1. First you may need to create the user under `root`.
Let's say we need to add the new `sentry` user:

    ```bash
    adduser sentry
    ```

    you'll see the output like that:

    ```
    Adding user `sentry' ...
    Adding new group `sentry' (1000) ...
    Adding new user `sentry' (1000) with group `sentry' ...
    Creating home directory `/home/sentry' ...
    Copying files from `/etc/skel' ...
    Enter new UNIX password: 
    ```

2. Then add the new user to the `sudo` group:

    ```bash
    usermod -aG sudo sentry
    ```

### Another way

1. Open the `/etc/sudoers` directly:

    ```bash
    visudo
    ```

    or

    ```bash
    vi /etc/sudoers
    ```

2. Add a new line for the specific user to sudoers file:

    ```
    # User alias specification
    sentry    ALL=(ALL:ALL) ALL
    ```

### Related articles

- [Add a User to a Group (or Second Group) on Linux](http://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/)
- [How To Edit the Sudoers File on Ubuntu and CentOS](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos)

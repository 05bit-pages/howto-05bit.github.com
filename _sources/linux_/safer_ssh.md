---
title: Safer SSH
---

How to configure SSH server for better security?
================================================

Default SSH configuration on most Linux distributions is relied on password authentication, which is not that much secure.

### Basic steps

1. Add your public key to `~/.ssh/authorized_keys`:

    ```bash
    mkdir -p ~/.ssh &&\
    chmod 700 ~/.ssh &&\
    cat > ~/.ssh/authorized_keys
    ```

    (^D to save)

2. Edit the `/etc/ssh/sshd_config`:

    ```bash
    vi /etc/ssh/sshd_config
    ```

    add or update the following settings

    ```
    ChallengeResponseAuthentication no
    PasswordAuthentication no
    UsePAM yes
    ```

3. Restart SSH server:

    ```bash
    service ssh restart
    ```

### Next steps

Add more tweaks to `/etc/ssh/sshd_config`.

1. Change the SSH server port, set the value for port different from `22`

    ````
    Port 1022
    ````

2. **Important!** Before this step set up [sudoers](../sudoers/) first and add `~/.ssh/authorized_keys` for the new users!

    ```bash
    mkdir -p /home/SOME_USER/.ssh &&\
    chown SOME_USER:SOME_USER /home/SOME_USER/.ssh &&\
    chmod 700 /home/SOME_USER/.ssh &&\
    cat > /home/SOME_USER/.ssh/authorized_keys
    ```

    **Login under SOME_USER, not the `root`!** Because we are going to disable login for the `root`!

    ```bash
    sudo vi /etc/ssh/sshd_config
    ```

    add or update the setting

    ````
    PermitRootLogin no
    ````

3. Restart SSH server:

    ```bash
    sudo service ssh restart
    ```

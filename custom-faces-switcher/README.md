# PWNAGOTCHI v1.5.5 - Faces MOD Switcher
Turn On/Off the [Pwnagotchi Faces MOD](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)


## Requirements
First and foremost, keep in mind that you must meet this requirements:
- A computer;
- The pwnagotchi `MUST BE` with the tutorial changes, including folder names and files. If you don't know what you're doing, it's better that way.

## Observations
The following steps were performed on a Windows computer using PuTTY as an SSH client, FileZilla and the pwnagotchi with a Waveshare 2.13 V3 e-ink display.
You should adapt them according to your configuration. This tutorial requires a minimum level of knowledge.

## The Script

First, with the pwnagotchi connected to a computer in `MANU` mode, establish an SSH connection.

Login as root:
```console
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi#
root@pwnagotchi:/home/pi# whoami
root
```


Navigate to root directory:
```console
root@pwnagotchi:/home/pi# cd /
```


Let's create the script folder:
```console
root@pwnagotchi:/# mkdir custom-faces-switcher
```



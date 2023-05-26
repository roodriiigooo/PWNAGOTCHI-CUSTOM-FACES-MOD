# PWNAGOTCHI v1.5.5 - Custom Faces Mod (⌐■_■)
Project for those who are tired of the same old string faces.
This mod allows you to use custom images as pwnagotchi Faces, with transparency feature (.png)

## Requirements
First and foremost, keep in mind that you must meet this requirements:
- A computer;
- The pwnagotchi must already be on the latest version (officially v1.5.5) properly configured;
- Perform a complete backup before making any modifications, including every file to be modified.

## Observations:
The following steps were performed on a Windows computer using PuTTY as an SSH client, FileZilla and the pwnagotchi with a Waveshare 2.13 V3 e-ink display.
You should adapt them according to your configuration. This tutorial requires a minimum level of knowledge.

## How to

1. First, with the pwnagotchi connected to a computer in MANU mode, establish an SSH connection.
2. Login as root:
```console
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi#
root@pwnagotchi:/home/pi# whoami
root
```
3. Navigate to root directory:
```console
root@pwnagotchi:/home/pi# cd /
```
4. Let's create two folders, one for backing up the files and another one to receive the custom faces:
```console
root@pwnagotchi:/home/pi# mkdir files-backup
root@pwnagotchi:/home/pi# mkdir custom-faces
```
5. Now let's navigate to the folder that contains the files we're going to modify:
```console
root@pwnagotchi:/home/pi# cd /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui
```
6. Stop the pwnagotchi service
```console
root@pwnagotchi:/home/pi# systemctl stop pwnagotchi
```
7. Here are the following files:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# ls
components.py  faces.py  hw           __pycache__  view.py
display.py     fonts.py  __init__.py  state.py     web
```
8. Now run the following command to make a backup of the first file:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# cp faces.py /files-backup/
```
9. Open the file using nano:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# nano faces.py
```
10. Add these attributes to the code, resulting in the following:
```python
...
UPLOAD1 = '(1__1)'
UPLOAD2 = '(0__1)'
PNG = False
POSITION_X = 40
POSITION_Y = 0

def load_from_config(config):
    for face_name, face_value in config.items():
        globals()[face_name.upper()] = face_value
...
```

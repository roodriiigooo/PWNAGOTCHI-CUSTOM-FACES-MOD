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

First, with the pwnagotchi connected to a computer in MANU mode, establish an SSH connection.

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
Let's create two folders, one for backing up the files and another one to receive the custom faces:
```console
root@pwnagotchi:/home/pi# mkdir files-backup
root@pwnagotchi:/home/pi# mkdir custom-faces
```
Now let's navigate to the folder that contains the files we're going to modify:
```console
root@pwnagotchi:/home/pi# cd /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui
```
Stop the pwnagotchi service
```console
root@pwnagotchi:/home/pi# systemctl stop pwnagotchi
```
Here are the following files:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# ls
components.py  faces.py  hw           __pycache__  view.py
display.py     fonts.py  __init__.py  state.py     web
```
Now run the following command to make a backup of the first file:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# cp faces.py /files-backup/
```
Open the file using nano:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# nano faces.py
```
Add these attributes to the code, resulting in the following:
```python
...
UPLOAD1 = '(1__1)'
UPLOAD2 = '(0__1)'
PNG = False
POSITION_X = 0
POSITION_Y = 40

def load_from_config(config):
    for face_name, face_value in config.items():
        globals()[face_name.upper()] = face_value
...
```
CTRL + O to save, CTRL + X to close file.

Now let's move on to the next file. Backup first, then edit:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# cp components.py /files-backup/
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# nano components.py
```
Locate this code snippet:
```python
class Text(Widget):
    def __init__(self, value="", position=(0, 0), font=None, color=0, wrap=False, max_length=0):
        super().__init__(position, color)
        self.value = value
        self.font = font
        self.wrap = wrap
        self.max_length = max_length
        self.wrapper = TextWrapper(width=self.max_length, replace_whitespace=False) if wrap else None

    def draw(self, canvas, drawer):
        if self.value is not None:
            if self.wrap:
                text = '\n'.join(self.wrapper.wrap(self.value))
            else:
                text = self.value
            drawer.text(self.xy, text, font=self.font, fill=self.color)
```
Now replace with:
```python
class Text(Widget):
    def __init__(self, value="", position=(0, 0), font=None, color=0, wrap=False, max_length=0, png=False):
        super().__init__(position, color)
        self.value = value
        self.font = font
        self.wrap = wrap
        self.max_length = max_length
        self.wrapper = TextWrapper(width=self.max_length, replace_whitespace=False) if wrap else None
        self.png = png

    def draw(self, canvas, drawer):
        if self.value is not None:
            if not self.png:
                if self.wrap:
                    text = '\n'.join(self.wrapper.wrap(self.value))
                else:
                    text = self.value
                drawer.text(self.xy, text, font=self.font, fill=self.color)
            else:
                self.image = Image.open(self.value)
                self.image = self.image.convert('RGBA')
                self.pixels = self.image.load()
                for y in range(self.image.size[1]):
                    for x in range(self.image.size[0]):
                        if self.pixels[x,y][3] < 255:    # check alpha
                            self.pixels[x,y] = (255, 255, 255, 255)
                if self.color == 255:
                    self._image = ImageOps.colorize(self.image.convert('L'), black = "white", white = "black")
                else:
                    self._image = self.image
                self.image = self._image.convert('1')
                canvas.paste(self.image, self.xy)
```
CTRL + O to save, CTRL + X to close file.

Now let's move on to the next file. Once again, backup first and then edit:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# cp view.py /files-backup/
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# nano view.py
```
Replace this one: 
```python
...
            'face': Text(value=faces.SLEEP, position=self._layout['face'], color=BLACK, font=fonts.Huge),
...
```
With that:
```python
...
	    'face': Text(value=faces.SLEEP, position=(config['ui']['faces']['position_x'], config['ui']['faces']['position_y']), color=BLACK, font=fonts.Huge, icon=config['ui']['faces']['icon']),
...
```
CTRL + O to save, CTRL + X to close file.

From this point on, the pwnagotchi is ready to display images instead of the default string.







# :star2: PWNAGOTCHI v1.5.5 - Custom Faces Mod (⌐■_■)
Project for those who are tired of the same old string faces.
This mod allows you to use custom images as pwnagotchi Faces, with transparency feature (.png) and themed plugins.


# :art: Themes List

Starting a collection of custom themes for pwnagotchi. Create your own and send me your pull request!

| Name                                                                                                                                                                                                                                                               | Without Optional Plugins                                                                                                                                    | With Optional Plugins                                                                                                                                     | Description                                    | Author                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| <p align="center"><img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/white-rabbit/WHITE_RABBIT.png?raw=true" height="48"> </br> [White Rabbit](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main/custom-themes/white-rabbit)</p>                                                                          |  <img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/white-rabbit/.screenshots/white-rabbit_screens.gif?raw=true">  |  -  |  Follow the White Rabbit... | [CodyTolene](https://github.com/CodyTolene)  |
| <p align="center"><img src="https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/assets/sideeye.gif?raw=true" height="48"> </br> [e-girl](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main/custom-themes/egirl-pwnagotchi)</p>                                                                          | ![Simple version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/egirl-pwnagotchi/.screenshots/ui.png?raw=true) |  ![Cool version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/egirl-pwnagotchi/.screenshots/ui_0.png?raw=true)  |  An amazing art by PersephoneKarnstein, was the inspiration for this project, check this out! | [PersephoneKarnstein](https://github.com/PersephoneKarnstein)  |
| <p align="center"><img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnachu/faces_pwnachu/PWNACHU_MINI.png?raw=true" height="48"> </br> [pwnachu](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main/custom-themes/pwnachu) </p> | ![Simple version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnachu/faces_pwnachu/.screenshots/ui_0.png?raw=true) | ![Cool version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnachu/faces_pwnachu/.screenshots/ui_1.png?raw=true) | A custom theme featuring my favorite character |    [roodriiigooo](https://github.com/roodriiigooo)    |                                                                                                                     |                                                |
| <p align="center"><img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/pwnaflipper/faces_flipper_dolphin/pwnaflipper_MINI.png?raw=true" height="48"> </br> [pwnaflipper](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main/custom-themes/pwnaflipper) </p> | ![Simple version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/pwnaflipper/faces_flipper_dolphin/.screenshots/ui_1.png?raw=true) | ![Cool version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/pwnaflipper/faces_flipper_dolphin/.screenshots/ui_0.png?raw=true) | A custom theme featuring Fliper Zero's character. Enjoy this crossover! |    [roodriiigooo](https://github.com/roodriiigooo)    |                                                                                                                     |                                                |
| <p align="center"><img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/pwnaflowey/faces_pwnaflowey/pwnaflowey_MINI.png?raw=true" height="48"> </br> [pwnaflowey](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main/custom-themes/pwnaflowey) </p> | <img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/raw/main/custom-themes/pwnaflowey/faces_pwnaflowey/.screenshots/ui.gif?raw=true"> | - | Flowey is a fictional character and the main antagonist of Undertale, a role-playing video game created by Toby Fox |    [roodriiigooo](https://github.com/roodriiigooo)    |                                                                                                                     |                                                |



## :heavy_exclamation_mark: Requirements
First and foremost, keep in mind that you must meet this requirements:
- A computer;
- The pwnagotchi must already be [`v1.5.5`](https://github.com/evilsocket/pwnagotchi/releases/tag/v1.5.5) properly configured;
- Perform a complete backup before making any modifications, including every file to be modified.

> **Important**
> The following steps were performed on a `Windows` computer using `PuTTY` as SSH client, `FileZilla` as FTP client and the pwnagotchi with a `Waveshare 2.13 V3 e-ink display` running on a `RPI0W`.
>> If you will use it in another fork or hardware, please be aware that you might need to adapt what is shown here

> **Note**
> Anyone can contribute by making a pull request.
>> Don't limit yourself to just this article, feel free to create your own themes!


> **Note**
> This tutorial requires a minimum level of knowledge.


## :heavy_exclamation_mark::heavy_exclamation_mark:  Disclaimer
> **Warning**
> From **roodriiigooo**: The content here is free for use, but it doesn't mean you can use it however you want. No author or contributor assumes responsibility for the misuse of this device, project, or any component herein. The project and modifications were **developed solely for educational purposes**.
> Any files, plugins or modifications of this project or original project found here should **not be sold**. In the case of use in open projects, videos or any form of dissemination, please remember to give credit to the repository ♥

> **Warning**
> Certain content may be protected by copyright, use with caution.


## :bookmark_tabs: Get Started

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
Let's create two folders, one for backing up the files and another one to receive the custom faces:
```console
root@pwnagotchi:/# mkdir files-backup
root@pwnagotchi:/# mkdir custom-faces
```
Now let's navigate to the folder that contains the files we're going to modify:
```console
root@pwnagotchi:/# cd /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui
```
Stop the pwnagotchi service
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# systemctl stop pwnagotchi
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
	    'face': Text(value=faces.SLEEP, position=(config['ui']['faces']['position_x'], config['ui']['faces']['position_y']), color=BLACK, font=fonts.Huge, png=config['ui']['faces']['png']),
...
```
CTRL + O to save, CTRL + X to close file.

From this point on, the pwnagotchi is ready to display images instead of the default string.

## :page_with_curl: Configuration
From here, we will able configure the images for our custom Faces. So lets do that!

Prepare the files, there are a total of `25`. I use images of size `128x45`. To make it easier, name the files according to the facial expression or emotion:
> **_Default .png file names:_**  

~~~
LOOK_R, LOOK_L, LOOK_R_HAPPY, LOOK_L_HAPPY, SLEEP, SLEEP2, AWAKE, BORED, INTENSE, COOL, HAPPY, GRATEFUL, EXCITED, MOTIVATED, DEMOTIVATED, LONELY, SAD, ANGRY, FRIEND, BROKEN, DEBUG, UPLOAD, UPLOAD1, UPLOAD2, ICON, POSITION_X, POSITION_Y
~~~

Stop the pwnagotchi service, if its not:
```console
root@pwnagotchi:/# systemctl stop pwnagotchi
```

### :flower_playing_cards: Upload Images
Use `FileZilla` or any other method you know to upload your images to the `/custom-faces/` folder that was created earlier.

> **Note**
> If you don't have it, use one of my theme packages from [here](#art-themes-list)

Open the pwnagotchi's configuration file:
```console
root@pwnagotchi:/# nano /etc/pwnagotchi/config.toml
```
Locate this code snippet:
```python
...
ui.faces.look_r = "( ⚆_⚆)"
ui.faces.look_l = "(☉_☉ )"
ui.faces.look_r_happy = "( ◕‿◕)"
ui.faces.look_l_happy = "(◕‿◕ )"
ui.faces.sleep = "(⇀‿‿↼)"
ui.faces.sleep2 = "(≖‿‿≖)"
ui.faces.awake = "(◕‿‿◕)"
ui.faces.bored = "(-__-)"
ui.faces.intense = "(°▃▃°)"
ui.faces.cool = "(⌐■_■)"
ui.faces.happy = "(•‿‿•)"
ui.faces.excited = "(ᵔ◡◡ᵔ)"
ui.faces.grateful = "(^‿‿^)"
ui.faces.motivated = "(☼‿‿☼)"
ui.faces.demotivated = "(≖__≖)"
ui.faces.smart = "(✜‿‿✜)"
ui.faces.lonely = "(ب__ب)"
ui.faces.sad = "(╥☁╥ )"
ui.faces.angry = "(-_-')"
ui.faces.friend = "(♥‿‿♥)"
ui.faces.broken = "(☓‿‿☓)"
ui.faces.debug = "(#__#)"
ui.faces.upload = "(1__0)"
ui.faces.upload1 = "(1__1)"
ui.faces.upload2 = "(0__1)"
...
```

This snippet will be responsible for enabling our customization. If it doesn't exist, you can add it.

Add the new entries pointing to the folder where the images were placed, set the position where the custom Face will be displayed and set the activation flag to `True`.

```python
...
ui.faces.look_r = "/custom-faces/LOOK-R.png"
ui.faces.look_l = "/custom-faces/LOOK-L.png"
ui.faces.look_r_happy = "/custom-faces/LOOK-R-HAPPY.png"
ui.faces.look_l_happy = "/custom-faces/LOOK-L-HAPPY.png"
ui.faces.sleep = "/custom-faces/SLEEP.png"
ui.faces.sleep2 = "/custom-faces/SLEEP2.png"
ui.faces.awake = "/custom-faces/AWAKE.png"
ui.faces.bored = "/custom-faces/BORED.png"
ui.faces.intense = "/custom-faces/INTENSE.png"
ui.faces.cool = "/custom-faces/COOL.png"
ui.faces.happy = "/custom-faces/HAPPY.png"
ui.faces.excited = "/custom-faces/EXCITED.png"
ui.faces.grateful = "/custom-faces/GRATEFUL.png"
ui.faces.motivated = "/custom-faces/MOTIVATED.png"
ui.faces.demotivated = "/custom-faces/DEMOTIVATED.png"
ui.faces.smart = "/custom-faces/SMART.png"
ui.faces.lonely = "/custom-faces/LONELY.png"
ui.faces.sad = "/custom-faces/SAD.png"
ui.faces.angry = "/custom-faces/ANGRY.png"
ui.faces.friend = "/custom-faces/FRIEND.png"
ui.faces.broken = "/custom-faces/BROKEN.png"
ui.faces.debug = "/custom-faces/DEBUG.png"
ui.faces.upload = "/custom-faces/UPLOAD.png"
ui.faces.upload1 = "/custom-faces/UPLOAD1.png"
ui.faces.upload2 = "/custom-faces/UPLOAD2.png"
ui.faces.png = true
ui.faces.position_x = 0
ui.faces.position_y = 34
...
```

> **Note**
> **_1:_** Check if your installed plugins modify the 'faces'. If there are any, replace them with the equivalent custom image address. If you don't do this, the pwnagotchi may crash. The code looks like this: `ui.set('face', "(◕‿‿◕)")` or `view.set('face', "(◕‿‿◕)")`

> **Note**
> **_2:_** I recommend that you always use the same path (`/custom-faces/` folder) for your customization. That way, it becomes easier as you only need to replace the files!

CTRL + O to save, CTRL + X to close file.

Restart your device
```console
root@pwnagotchi:/# systemctl restart pwnagotchi
```

Enjoy!

## :writing_hand: How to Contribute?
> This is an entirely open project that accepts contributions via pull requests, your name will be placed as an author. If you have any questions, please open an issue.
1. Create a fork of this repository
2. Create your theme following the pattern of the ones already posted
3. Commit your changes in English
4. Include a brief summary of what was added
5. Submit your pull request

## :triangular_flag_on_post: Whats Next?
- [x] Update the docs for pwnagotchi `v1.5.5`
- [ ] Buy new hardware
- [ ] Mod for new forks (newer versions)


## :pill: Troubleshooting
- Check the log file, read and interpret:
```console
root@pwnagotchi:/# tail -f /var/log/pwnagotchi.log
```
- Restore the backup files that we placed in `/files-backup/` and try again

- If you don't have permission, try `chmod 777`

- Make sure that **all entries related to the plugins** are indeed in the `config.toml` file

- PM me [here](https://github.com/roodriiigooo/) 


## :star: Discover another projects
- [Fancygotchi](https://github.com/V0r-T3x/fancygotchi) by [V0r-T3x](https://github.com/V0r-T3x)


## :tophat: Thank You ♥
[Evilsocket](https://github.com/evilsocket/pwnagotchi) - [PersephoneKarnstein](https://github.com/PersephoneKarnstein) - [V0r-T3x](https://github.com/V0r-T3x) - [@demetrius_official](https://instagram.com/demetrius_official)

## :sparkling_heart: Support Me 
> If you like my work and want to support me, plz consider

<a href="https://www.buymeacoffee.com/rodrigoo" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-5C3317?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white" alt="Buy Me A Coffee" target="_blank"></a>
<a href="https://www.paypal.com/donate/?business=RNSQFDU927P8A&no_recurring=0&item_name=Every+penny+donated+is+an+investment+not+only+in+me+but+also+in+fulfilling+dreams+and+creating+opportunities.&currency_code=BRL" target="_blank"><img src="https://img.shields.io/badge/Paypal%20%28BRL%29-4287f5?style=for-the-badge&logo=paypal&logoColor=white" alt="Paypal" target="_blank"></a>



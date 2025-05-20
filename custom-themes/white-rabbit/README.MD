# White Rabbit

**Follow the White Rabbit...**

<img height="48" src="WHITE_RABBIT.png?raw=true" style="invert(100%);" />

## Installation

<details>
  <summary>
    Click here to expand/collapse.
  </summary>

## Requirements

First and foremost, keep in mind that you must meet this requirements:

- Having followed all the steps in [this tutorial][link-tutorial].

## How To

With the pwnagotchi connected to a computer in `MANU` mode, establish an SSH connection.

Place the images from the `_faces` folder into your custom faces folder.

Login as root:

```console
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi#
root@pwnagotchi:/home/pi# whoami
root
root@pwnagotchi:/home/pi# cd /
```

Stop pwnagotchi service:

```console
root@pwnagotchi:/# systemctl stop pwnagotchi
```

Assuming you have already downloaded this project, upload the images using `FileZilla` or your preferred method to the custom faces folder created during [this tutorial][link-tutorial].

Open the pwnagotchi's configuration file:

```console
root@pwnagotchi:/# nano /etc/pwnagotchi/config.toml
```

Add or replace the new entries pointing to the folder where the images were placed, set the position (x, y) where the custom Face will be displayed and set the activation flag to `True`.

> **_Note 1:_** Check if your installed plugins modify the 'faces'. If there are any, replace them with the equivalent custom image address. If you don't do this, the pwnagotchi may crash. The code looks like this: `ui.set('face', "(◕‿‿◕)")` or `view.set('face', "(◕‿‿◕)")`.

> **_Note 2:_** I recommend that you always use the same path (`/custom-faces/` folder) for your customization. That way, it becomes easier as you only need to replace the files!

> **_Note 3:_** The following position settings are for the display "waveshare144lcd", update as needed.

```python
...
ui.faces.look_r = "/custom-faces/LOOK_R.png"
ui.faces.look_l = "/custom-faces/LOOK_L.png"
ui.faces.look_r_happy = "/custom-faces/LOOK_R_HAPPY.png"
ui.faces.look_l_happy = "/custom-faces/LOOK_L_HAPPY.png"
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

CTRL + O to save, CTRL + X to close file.

Reboot pwnagotchi service:

```console
root@pwnagotchi:/# systemctl restart pwnagotchi
```

Reboot pwnagotchi service again:

```console
root@pwnagotchi:/# systemctl restart pwnagotchi
```

## Hint

If the status of your pwnagotchi is misaligned or if you want to change the position of the text, you can edit the screen configuration file. In my case, it is located at:

```console
root@pwnagotchi:/# nano /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/waveshare144lcd.py
```

Look for:

```python
        self._layout['status'] = {
            'pos': (125, 20),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }

```

And put whatever position you want in `pos` (x, y).

In my case:

```python
        self._layout['status'] = {
            'pos': (125, 34),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }

```

CTRL + O to save, CTRL + X to close file.

Reboot pwnagotchi service again to complete the process:

```console
root@pwnagotchi:/# systemctl restart pwnagotchi
```

</details>

## Sprite Table

| Emotion                                       | Original | Replacement                       | Emotion (cont'd)                | Original | Replacement                 |
| --------------------------------------------- | -------- | --------------------------------- | ------------------------------- | -------- | --------------------------- |
| LOOK_R                                        | `( ⚆_⚆)` | ![Look_R][img-look-r]             | GRATEFUL                        | `(^‿‿^)` | ![Grateful][img-grateful]   |
| LOOK_L                                        | `(☉_☉ )` | ![Look_L][img-look-l]             | EXCITED                         | `(ᵔ◡◡ᵔ)` | ![Excited][img-excited]     |
| LOOK_R_HAPPY                                  | `( ◕‿◕)` | ![Look_R_Happy][img-look-r-happy] | MOTIVATED                       | `(☼‿‿☼)` | ![Motivated][img-motivated] |
| LOOK_L_HAPPY                                  | `(◕‿◕ )` | ![Look_L_Happy][img-look-l-happy] | DEMOTIVATED                     | `(≖__≖)` | ![Bored][img-bored]         |
| SLEEP <br/> _(long sleep)_                    | `(⇀‿‿↼)` | ![Sleep][img-sleep]               | SMART <br/> _(on free channel)_ | `(✜‿‿✜)` | ![Smart][img-smart]         |
| SLEEP2 <br/> _(short sleep)_                  | `(≖‿‿≖)` | ![Sleep2][img-sleep2]             | LONELY                          | `(ب__ب)` | ![Lonely][img-lonely]       |
| AWAKE                                         | `(◕‿‿◕)` | ![Awake][img-awake]               | SAD _(on miss)_                 | `(╥☁╥ )` | ![Sad][img-sad]             |
| BORED                                         | `(-__-)` | ![Bored][img-bored]               | ANGRY                           | `(-_-')` | ![Angry][img-angry]         |
| INTENSE <br/> _(successful wifi association)_ | `(°▃▃°)` | ![Intense][img-intense]           | FRIEND                          | `(♥‿‿♥)` | ![Friend][img-friend]       |
| COOL <br/> _(on deauth)_                      | `(⌐■_■)` | ![Cool][img-cool]                 | BROKEN <br/> _(on reboot)_      | `(☓‿‿☓)` | ![Broken][img-broken]       |
| HAPPY <br/> _(new handshakes)_                | `(•‿‿•)` | ![Happy][img-happy]               | DEBUG <br/>                     | `(#__#)` | ![Debug][img-debug]         |
| UPLOAD                                        | `(1__0)` | ![Upload][img-upload]             | UPLOAD1                         | `(1__1)` | ![Upload1][img-upload1]     |
| UPLOAD2                                       | `(0__1)` | ![Upload2][img-upload2]           |

**Enjoy!**

Cody Tolene &#60;<a href="mailto:webmaster@codytolene.com">Email</a> | <a href="https://github.com/CodyTolene">GitHub</a>&#62;

<!-- IMAGES -->

[img-angry]: _faces/ANGRY.png?raw=true
[img-awake]: _faces/AWAKE.png?raw=true
[img-bored]: _faces/BORED.png?raw=true
[img-broken]: _faces/BROKEN.png?raw=true
[img-cool]: _faces/COOL.png?raw=true
[img-debug]: _faces/DEBUG.png?raw=true
[img-excited]: _faces/EXCITED.png?raw=true
[img-friend]: _faces/FRIEND.png?raw=true
[img-grateful]: _faces/GRATEFUL.png?raw=true
[img-happy]: _faces/HAPPY.png?raw=true
[img-intense]: _faces/INTENSE.png?raw=true
[img-lonely]: _faces/LONELY.png?raw=true
[img-look-l-happy]: _faces/LOOK_L_HAPPY.png?raw=true
[img-look-l]: _faces/LOOK_L.png?raw=true
[img-look-r-happy]: _faces/LOOK_R_HAPPY.png?raw=true
[img-look-r]: _faces/LOOK_R.png?raw=true
[img-motivated]: _faces/MOTIVATED.png?raw=true
[img-sad]: _faces/SAD.png?raw=true
[img-sleep2]: _faces/SLEEP2.png?raw=true
[img-sleep]: _faces/SLEEP.png?raw=true
[img-smart]: _faces/SMART.png?raw=true
[img-upload]: _faces/UPLOAD.png?raw=true
[img-upload1]: _faces/UPLOAD1.png?raw=true
[img-upload2]: _faces/UPLOAD2.png?raw=true

<!-- LINKS -->

[link-tutorial]: https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD?tab=readme-ov-file#bookmark_tabs-get-started

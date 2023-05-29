# <img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/pwnaflipper_MINI.png?raw=true" height="48"> pwnaflipper

A custom theme featuring Fliper Zero's character. Enjoy this crossover!

|                                  Without Optional Plugins                                            |                                            With Optional Plugins                                                     |
| :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: |
|                                                ![Simple version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/.screenshots/ui_1.png?raw=true)    |           ![Cool version](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/.screenshots/ui_0.png?raw=true)  |


## Requirements
First and foremost, keep in mind that you must meet this requirements:
- Having followed all the steps in [this tutorial](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main#pwnagotchi-v155---custom-faces-mod-_)

## How To
First, with the pwnagotchi connected to a computer in `MANU` mode, establish an SSH connection.

Login as root:
```console
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi#
root@pwnagotchi:/home/pi# whoami
root
root@pwnagotchi:/home/pi# cd /
```
Stop pwnagotchi service
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# systemctl stop pwnagotchi
```

Assuming you have already downloaded this project, upload the images using FileZilla or your preferred method to the custom faces folder created during [this tutorial](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/tree/main#pwnagotchi-v155---custom-faces-mod-_).

Open the pwnagotchi's configuration file:
```console
root@pwnagotchi:/# nano /etc/pwnagotchi/config.toml
```

Add or replace the new entries pointing to the folder where the images were placed, set the position where the custom Face will be displayed and set the activation flag to True.

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
ui.faces.icon = true
ui.faces.position_x = 0
ui.faces.position_y = 36
...
```
CTRL + O to save, CTRL + X to close file.

# Optional
Place the plugins from the `plugins_pwnaflipper` folder into your custom plugins folder path.

Edit `pwnaflipper-theme.py` with your `custom-faces` folder:
```python
...
            self.image0 = Frame(path=f'/custom-faces/{TOPBAR}', xy=(55, 82))
            self.image1 = Frame(path=f'/custom-faces/{NORMALBAR}', xy=(176, 36))
            self.image2 = Frame(path=f'/custom-faces/{SDCARDICON}', xy=(232, 18))
...
```

> **_Note:_** You can also replace `NORMALBAR` with `XPBAR` if you prefer. Remember to adjust (x, y). The `pwnaflipperexp.yml` file contains the entries that should be in the config.toml file for the `plugin` to work.


Reboot pwnagotchi service
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# systemctl restart pwnagotchi
```

Activate plugins `pwnaflipperexp` and `pwnaflipper-theme`


Reboot pwnagotchi service again
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# systemctl restart pwnagotchi
```

Enjoy!

---



|                                               Emotion                                                |                                                     Original                                                     |                                                                            Replacement                                                                             |     |               Emotion (cont'd)                |  Original  |                                                                            Replacement                                                                             |
| :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: | :-------------------------------------------: | :--------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                LOOK_R                                                |                                                     `( ⚆_⚆)`                                                     |                              ![Look_R](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/LOOK-R.png?raw=true)                              |     |                   GRATEFUL                    |  `(^‿‿^)`  | ![Grateful](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/GRATEFUL.png?raw=true)                                                       |
|                                                LOOK_L                                                |                                                     `(☉_☉ )`                                                     |                              ![Look_L](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/LOOK-L.png?raw=true)                              |     |      EXCITED <!-- on_unread_messages -->      |  `(ᵔ◡◡ᵔ)`  |                           ![Excited](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/EXCITED.png?raw=true)                               |
|                                             LOOK_R_HAPPY                                             |                                                     `( ◕‿◕)`                                                     |                              ![Look_R_Happy](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/LOOK-R-HAPPY.png?raw=true)                  |     |                   MOTIVATED                   |  `(☼‿‿☼)`  |                           ![Motivated](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/MOTIVATED.png?raw=true)                           |
|                                             LOOK_L_HAPPY                                             |                                                     `(◕‿◕ )`                                                     |                              ![Look_L_Happy](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/LOOK-L-HAPPY.png?raw=true)                  |     |                  DEMOTIVATED                  |  `(≖__≖)`  |                           ![Bored](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/BORED.png?raw=true)                                   |
|                            SLEEP <!-- long sleep --> <br/> *(long sleep)*                            |                                                     `(⇀‿‿↼)`                                                     |                              ![Sleep](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/SLEEP.png?raw=true)                                |     |        SMART <br/> *(on free channel)*        |  `(✜‿‿✜)`  |                           ![Smart](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/SMART.png?raw=true)                                   |
|                          SLEEP2 <!-- short sleep --> <br/> *(short sleep)*                           |                                                     `(≖‿‿≖)`                                                     |                              ![Sleep2](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/SLEEP2.png?raw=true)                              |     |                    LONELY                     |  `(ب__ب)`  |                           ![Lonely](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/LONELY.png?raw=true)                                 |
|                                                AWAKE                                                 |                                                     `(◕‿‿◕)`                                                     |                              ![Awake](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/AWAKE.png?raw=true)                                |     |             SAD <!-- on_miss -->              |  `(╥☁╥ )`  |                           ![Sad](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/SAD.png?raw=true)                                       |
|                                                BORED                                                 |                                                     `(-__-)`                                                     |                              ![Bored](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/BORED.png?raw=true)                                |     |                     ANGRY                     |  `(-_-')`  |                           ![Angry](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/ANGRY.png?raw=true)                                   |
| INTENSE <!-- on_assoc : post auth, data transfer can begin --> <br/> *(successful wifi association)* |                                                     `(°▃▃°)`                                                     | ![INTENSE](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/INTENSE.png?raw=true)                                                         |     |                    FRIEND                     |  `(♥‿‿♥)`  |                           ![Friend](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/FRIEND.png?raw=true)                                 |
|                                       COOL <!-- on_deauth -->                                        |                                                     `(⌐■_■)`                                                     |                              ![Cool](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/COOL.png?raw=true)                                  |     | BROKEN <!-- on_reboot --> <br/> *(on reboot)* |  `(☓‿‿☓)`  |                           ![Broken](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/BROKEN.png?raw=true)                                 |
|                                    HAPPY <!-- new handshakes -->                                     |                                                     `(•‿‿•)`                                                     |                              ![Happy](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/HAPPY.png?raw=true)                                |     | DEBUG <!-- on_custom --> <br/> *(on custom)*  |  `(#__#)`  |                           ![Debug](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/DEBUG.png?raw=true)                                   |
|                                            UPLOAD [ /1/2]                                            | <img src="https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD/blob/main/custom-themes/pwnaflipper/faces_flipper_dolphin/UPLOAD.png?raw=true" height="64">                          |     |                                               |            |                                                                                                                                                                    |

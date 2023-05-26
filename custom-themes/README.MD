# <img src="https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/assets/sideeye.gif?raw=true" height="48"> pwnagotchi e-girl

### Background

At time of writing, the pwnagotchi only allows single line, text-based emoji to be used as faces for its moods. While these faces can be edited (by editing [pwnagotchi/pwnagotchi/ui/faces.py](https://github.com/evilsocket/pwnagotchi/blob/decbeaccb1b3a3b4364204478c7987df0104edf1/pwnagotchi/ui/faces.py)), as written they can only be changed to different single-line emoji. The layout of the pwnagotchi's face is defined on [line 57 of pwnagotchi/pwnagotchi/ui/view.py](https://github.com/evilsocket/pwnagotchi/blob/a5d5533acf9ebf0d70b12b7631b5119aea5b7b3b/pwnagotchi/ui/view.py#L57), using the Text class defined in [pwnagotchi/pwnagotchi/ui/components.py](https://github.com/evilsocket/pwnagotchi/blob/a5d5533acf9ebf0d70b12b7631b5119aea5b7b3b/pwnagotchi/ui/components.py),

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

The same file also defines a [Bitmap class](https://github.com/evilsocket/pwnagotchi/blob/a5d5533acf9ebf0d70b12b7631b5119aea5b7b3b/pwnagotchi/ui/components.py#L14) which is never used, likely a holdover from work done towards fulfilling [requests](https://github.com/evilsocket/pwnagotchi/issues/47) to make BMP faces a feature going as far back as 2019.

```python
class Bitmap(Widget):
    def __init__(self, path, xy, color=0):
        super().__init__(xy, color)
        self.image = Image.open(path)

    def draw(self, canvas, drawer):
        canvas.paste(self.image, self.xy)
```

Because the pwnagotchi display is rendered on the fly[^1] we *should* be able to fairly simply replace the emoji defined in **faces.py** with custom images.

[^1]: (I think, but the code there is annoying and I'd rather poke at it than spend an hour glaring at it keeping track of all the `.super` and shit)

```python
class View(object):
    def __init__(self, config, impl, state=None):
        global ROOT

        # setup faces from the configuration in case the user customized them
        faces.load_from_config(config['ui']['faces'])
```
```python
        self._state = State(state={
```
```python
            'face': Text(value=faces.SLEEP, position=self._layout['face'], color=BLACK, font=fonts.Huge),
```
```python
            'status': Text(value=self._voice.default(),
                           position=self._layout['status']['pos'],
                           color=BLACK,
                           font=self._layout['status']['font'],
                           wrap=True,
                           # the current maximum number of characters per line, assuming each character is 6 pixels wide
                           max_length=self._layout['status']['max']),
```





---
## Goal

The aim of this project is to replace the text pwnagotchi face with bitmap faces in the absence of an update that does same. The faces used are all custom drawn by me and fit within a 64x64px square. Some examples are shown below.


|                                               Emotion                                                |                                                     Original                                                     |                                                                            Replacement                                                                             |     |               Emotion (cont'd)                |  Original  |                                                                            Replacement                                                                             |
| :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: | :-------------------------------------------: | :--------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                LOOK_R                                                |                                                     `( ⚆_⚆)`                                                     |                              ![Look_R](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/LOOK-R.png?raw=true)                              |     |                   GRATEFUL                    |  `(^‿‿^)`  | ![Grateful](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/GRATEFUL.png?raw=true) <!-- I refuse to draw her doing aheago. fight me. --> |
|                                                LOOK_L                                                |                                                     `(☉_☉ )`                                                     |                              ![Look_L](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/LOOK-L.png?raw=true)                              |     |      EXCITED <!-- on_unread_messages -->      |  `(ᵔ◡◡ᵔ)`  |                           ![Excited](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/EXCITED.png?raw=true)                               |
|                                             LOOK_R_HAPPY                                             |                                                     `( ◕‿◕)`                                                     |                              ![Look_R_Happy](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/LOOK-R-HAPPY.png?raw=true)                  |     |                   MOTIVATED                   |  `(☼‿‿☼)`  |                           ![Motivated](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/MOTIVATED.png?raw=true)                           |
|                                             LOOK_L_HAPPY                                             |                                                     `(◕‿◕ )`                                                     |                              ![Look_L_Happy](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/LOOK-L-HAPPY.png?raw=true)                  |     |                  DEMOTIVATED                  |  `(≖__≖)`  |                           ![Bored](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/BORED.png?raw=true)                                   |
|                            SLEEP <!-- long sleep --> <br/> *(long sleep)*                            |                                                     `(⇀‿‿↼)`                                                     |                              ![Sleep](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/SLEEP.png?raw=true)                                |     |        SMART <br/> *(on free channel)*        |  `(✜‿‿✜)`  |                           ![Smart](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/SMART.png?raw=true)                                   |
|                          SLEEP2 <!-- short sleep --> <br/> *(short sleep)*                           |                                                     `(≖‿‿≖)`                                                     |                              ![Sleep2](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/SLEEP2.png?raw=true)                              |     |                    LONELY                     |  `(ب__ب)`  |                           ![Lonely](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/LONELY.png?raw=true)                                 |
|                                                AWAKE                                                 |                                                     `(◕‿‿◕)`                                                     |                              ![Awake](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/AWAKE.png?raw=true)                                |     |             SAD <!-- on_miss -->              |  `(╥☁╥ )`  |                           ![Sad](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/SAD.png?raw=true)                                       |
|                                                BORED                                                 |                                                     `(-__-)`                                                     |                              ![Bored](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/BORED.png?raw=true)                                |     |                     ANGRY                     |  `(-_-')`  |                           ![Angry](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/ANGRY.png?raw=true)                                   |
| INTENSE <!-- on_assoc : post auth, data transfer can begin --> <br/> *(successful wifi association)* |                                                     `(°▃▃°)`                                                     | ![Avatar](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/AVATAR.png?raw=true) <!-- There's also an Anonymous one you could use here --> |     |                    FRIEND                     |  `(♥‿‿♥)`  |                           ![Friend](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/FRIEND.png?raw=true)                                 |
|                                       COOL <!-- on_deauth -->                                        |                                                     `(⌐■_■)`                                                     |                              ![Cool](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/COOL.png?raw=true)                                  |     | BROKEN <!-- on_reboot --> <br/> *(on reboot)* |  `(☓‿‿☓)`  |                           ![Broken](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/BROKEN.png?raw=true)                                 |
|                                    HAPPY <!-- new handshakes -->                                     |                                                     `(•‿‿•)`                                                     |                              ![Happy](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/HAPPY.png?raw=true)                                |     | DEBUG <!-- on_custom --> <br/> *(on custom)*  |  `(#__#)`  |                           ![Debug](https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/faces/DEBUG.png?raw=true)                                   |
|                                            UPLOAD [ /1/2]                                            | <img src="https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/assets/upload-old.gif" width="60"> |                         <img src="https://github.com/PersephoneKarnstein/egirl-pwnagotchi/blob/master/assets/upload-new.gif" height="64">                          |     |                                               |            |                                                                                                                                                                    |

# Rickgotchi

**Rickgotchi** is a custom skin for Pwnagotchi featuring the legendary face and quotes of Rick Sanchez from "Rick and Morty". This mod replaces the default ASCII faces and optionally the voice system, giving your AI companion more character, sarcasm, and science.

---

## ⚙️ Setup Instructions

### 1. Replace Default Faces

Open your Pwnagotchi configuration file:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Find and **replace the entire block** that looks like this:

```toml
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
ui.faces.png = false
ui.faces.position_x = 0
ui.faces.position_y = 34
```

**With this Rickgotchi version:**

```toml
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
```

Make sure all the PNG files are placed under a directory called `/custom-faces/` in the root (`/`) of your system. You can copy the folder from this repository:

```bash
sudo cp -r /path/to/rickgotchi-repo/custom-faces /custom-faces
```

---

### 2. Replace the Voice File (Optional)

Replace the `voice.py` file to give your Rickgotchi a unique personality with Rick’s iconic style.

Run the following command to find the location of `voice.py` on your device:

```bash
sudo find / -name voice.py 2>/dev/null
```

Typical path (example):

```
/usr/local/lib/python3.11/dist-packages/pwnagotchi/voice.py
```

Then, replace it with your custom version:

```bash
sudo cp /path/to/your/custom/voice.py /usr/local/lib/python3.11/dist-packages/pwnagotchi/voice.py
```

---

### 3. Use Rickgotchi in German

If you want Rickgotchi to speak German, replace the default translation files:

1. Copy the German `.mo` and `.po` files from this repository:

```bash
sudo cp voice.mo /usr/local/lib/python3.11/dist-packages/pwnagotchi/locale/de/LC_MESSAGES/
sudo cp voice.po /usr/local/lib/python3.11/dist-packages/pwnagotchi/locale/de/LC_MESSAGES/
```

2. Then open your config file and change the language:

```toml
main.lang = "de"
```

---

Enjoy your Rickgotchi — a smarter, ruder, and way cooler version of Pwnagotchi.

> *"Wubba Lubba Dub Dub! Now go own some packets."*

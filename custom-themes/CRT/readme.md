# CRT

**CRT** is a custom skin for Pwnagotchi featuring Edgar from "Electric Dreams (1984) (You should guve it a watch!). This mod replaces the default ASCII faces of the pwnagotchi.

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

**With this CRT version:**

```toml
ui.faces.look_r = "/custom-faces/look-r.png"
ui.faces.look_l = "/custom-faces/look-l.png"
ui.faces.look_r_happy = "/custom-faces/look-r-happy.png"
ui.faces.look_l_happy = "/custom-faces/look-l-happy.png"
ui.faces.sleep = "/custom-faces/sleep.png"
ui.faces.sleep2 = "/custom-faces/sleep2.png"
ui.faces.awake = "/custom-faces/awake.png"
ui.faces.bored = "/custom-faces/bored.png"
ui.faces.intense = "/custom-faces/intense.png"
ui.faces.cool = "/custom-faces/cool.png"
ui.faces.happy = "/custom-faces/happy.png"
ui.faces.excited = "/custom-faces/excited.png"
ui.faces.grateful = "/custom-faces/grateful.png"
ui.faces.motivated = "/custom-faces/motivated.png"
ui.faces.demotivated = "/custom-faces/demotivated.png"
ui.faces.smart = "/custom-faces/smart.png"
ui.faces.lonely = "/custom-faces/lonely.png"
ui.faces.sad = "/custom-faces/sad.png"
ui.faces.angry = "/custom-faces/angry.png"
ui.faces.friend = "/custom-faces/friend.png"
ui.faces.broken = "/custom-faces/broken.png"
ui.faces.debug = "/custom-faces/debug.png"
ui.faces.upload = "/custom-faces/upload.png"
ui.faces.upload1 = "/custom-faces/upload1.png"
ui.faces.upload2 = "/custom-faces/upload2.png"
ui.faces.png = true
ui.faces.position_x = 0
ui.faces.position_y = 34
```

Make sure all the PNG files are placed under a directory called `/custom-faces/` in the root (`/`) of your system. You can copy the folder from this repository:

```bash
sudo cp -r /path/to/crt-repo/custom-faces /custom-faces
```

---

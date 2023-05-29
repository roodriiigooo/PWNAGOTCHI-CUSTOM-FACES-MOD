import os
import random
from PIL import Image, ImageDraw, ImageFont
from pwnagotchi.ui.components import *
import pwnagotchi.ui.faces as faces
import pwnagotchi.ui.fonts as fonts
import logging
import pwnagotchi.plugins as plugins
from pwnagotchi.ui.view import View
from pwnagotchi.ui.view import BLACK

NORMALBAR = 'NORMAL_BAR.png'
XPBAR = 'XP_BAR.png'  #optional, may replace NORMALBAR
SDCARDICON = 'SD_CARD_ICON.png'
TOPBAR = 'TOP_BAR.png'

class pwnaflipper(plugins.Plugin):
    __author__ = 'Rodrigo A. Melo'
    __version__ = '1.0.1'
    __license__ = 'MIT'
    __description__ = 'Tema complementar do Pwnaflipper faces'

    def __init__(self):
        try:
            logging.info("Loading PWNAFLIPPER frames")
        except Exception as e:
            logging.info(f'Failed to load init')

    def on_unload(self, ui):
        with ui._lock:
            try:
                ui.remove_element('topbar')
                ui.remove_element('btbar')
                ui.remove_element('icon')
                logging.info(f'PWNAFLIPPER frames unloaded')
            except Exception as e:
                logging.info(f'Failed to load face on on_unload: {e}')

    def on_ui_setup(self, ui):
        try:
            self.image0 = Frame(path=f'/custom-faces/{TOPBAR}', xy=(4, 16))
            self.image1 = Frame(path=f'/custom-faces/{NORMALBAR}', xy=(124, 79)) #or use XPBAR, adjust (x,y)
            self.image2 = Frame(path=f'/custom-faces/{SDCARDICON}', xy=(231, 20))
            ui.add_element('topbar', self.image0)
            ui.add_element('btbar', self.image1)
            ui.add_element('icon', self.image2)
            logging.info(f'PWNAFLIPPER frames loaded')
        except Exception as e:
            logging.info(f'Failed to load face on on_ui_setup: {e}' )

    def on_loaded(self):
        # logging.info("Exp plugin loaded for %s" % self.options['device'])
        self.LogInfo("PWNAFLIPPER frames plugin Loaded")


class Frame(Widget):
    def __init__(self, path, xy, alpha=0):
        super().__init__(xy)
        self.image = Image.open(path).convert('RGBA')
        self.alpha = alpha

    def draw(self, canvas, drawer):
        r, g, b, a = self.image.split()
        alpha = Image.new('L', self.image.size, self.alpha)
        canvas.paste(self.image, self.xy, mask=alpha)
        canvas.paste(alpha, self.xy, mask=a)
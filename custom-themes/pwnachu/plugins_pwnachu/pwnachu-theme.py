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

POKEBARXP = 'POKEBAR_XP_LEFT.png'
FRAMERIGHT = 'POKEBAR_RIGHT.png'
PWNACHUMINI = 'PWNACHU_MINI.png'

class pwnachu(plugins.Plugin):
    __author__ = 'Rodrigo A. Melo'
    __version__ = '1.0.1'
    __license__ = 'MIT'
    __description__ = 'Tema complementar do Pwnachu faces'

    def __init__(self):
        try:
            logging.info("Loading PWNACHU frames")
        except Exception as e:
            logging.info(f'Failed to load init')

    def on_unload(self, ui):
        with ui._lock:
            try:
                ui.remove_element('pokebarxp')
                ui.remove_element('frameright')
                ui.remove_element('pwnachumini')
                logging.info(f'PWNACHU frames unloaded')
            except Exception as e:
                logging.info(f'Failed to load face on on_unload: {e}')

    def on_ui_setup(self, ui):
        try:
            self.image0 = Frame(path=f'/custom-faces/{POKEBARXP}', xy=(55, 82))
            self.image1 = Frame(path=f'/custom-faces/{FRAMERIGHT}', xy=(176, 35))
            self.image2 = Frame(path=f'/custom-faces/{PWNACHUMINI}', xy=(232, 18))
            ui.add_element('pokebarxp', self.image0)
            ui.add_element('frameright', self.image1)
            ui.add_element('pwnachumini', self.image2)
            logging.info(f'PWNACHU frames loaded')
        except Exception as e:
            logging.info(f'Failed to load face on on_ui_setup: {e}' )

    def on_loaded(self):
        # logging.info("Exp plugin loaded for %s" % self.options['device'])
        self.LogInfo("PWNACHU frames plugin Loaded")


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
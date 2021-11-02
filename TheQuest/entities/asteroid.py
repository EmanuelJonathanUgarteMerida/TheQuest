import os
import pygame as pg
from pygame.sprite import Sprite

from TheQuest import RESOURCES


class Asteroid(Sprite):
    def __init__(self, name_image):
        super().__init__()
        self.image = pg.image.load(
            os.path.join(RESOURCES, 'image', name_image))
        self.type = ()
        self.pos_ini = 0
        self.create_asteroid()

    def create_asteroid(self):
        pass

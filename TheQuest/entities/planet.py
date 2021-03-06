import os
from pygame.sprite import Sprite
import pygame as pg

from TheQuest import IMAGES, RESOURCES, SC_HEIGHT, SC_WIDTH


class Planet(Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.bonus_points = self.level*100
        self.load_planet()
        self.rect = self.image.get_rect()
        self.rect.center = (SC_WIDTH/2, SC_HEIGHT/2)
        self.rect.x = SC_WIDTH

    def update(self):
        if self.rect.centerx > SC_WIDTH-100:
            self.rect.centerx -= 1

    def load_planet(self):
        self.image = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'planets', f'planet_{self.level}.png'))

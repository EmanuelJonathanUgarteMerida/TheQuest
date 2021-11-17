import os
import pygame as pg
from pygame.sprite import Sprite

from TheQuest import IMAGES, RESOURCES


class Bullet(Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'bullets', 'bullet.png'))
        self.rect = self.image.get_rect()
        self.rect.centery = y

    def update(self):
        self.rect.centerx += 1

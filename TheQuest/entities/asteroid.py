import os
import pygame as pg
from pygame.sprite import Sprite
from random import randint

from TheQuest import SC_HEIGHT, SC_WIDTH


class Asteroid(Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.create_asteroid()

    def create_asteroid(self):
        # random generating position
        x = randint(100, SC_WIDTH)
        y = randint(0, SC_HEIGHT)
        self.rect.center = (x, y)
        self.speed_x = randint(1, 3)
        self.level = 1

    def update(self, space_ship, *args, **kwargs):
        self.rect.x -= self.speed_x
        if self.rect.right <= space_ship.rect.left:
            space_ship.score += self.level
            self.kill()

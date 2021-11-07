import os
import pygame as pg
from pygame.sprite import Sprite
from random import randint

from TheQuest import SC_HEIGHT, SC_WIDTH


class Asteroid(Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.dodged = False
        self.rect = self.image.get_rect()
        self.create_asteroid()

    def create_asteroid(self):
        # random generating position
        x = randint(SC_WIDTH, SC_WIDTH+100)
        y = randint(0, SC_HEIGHT)
        self.rect.center = (x, y)
        self.level = randint(1, 3)
        self.speed_x = self.level

    def update(self, space_ship, *args, **kwargs):
        self.rect.x -= self.speed_x
        if self.rect.right < 0:
            space_ship.score += 1
            self.dodged = True
            self.kill()

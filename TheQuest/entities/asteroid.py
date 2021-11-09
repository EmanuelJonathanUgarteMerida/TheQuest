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
        self.speed_x = randint(1, 3)

    def create_asteroid(self):
        # random generating position
        x = randint(SC_WIDTH, SC_WIDTH+100)
        y = randint(0, SC_HEIGHT)
        self.rect.center = (x, y)

    def update(self, *args, **kwargs):
        self.rect.x -= self.speed_x
        if self.rect.right < 0:
            self.dodged = True

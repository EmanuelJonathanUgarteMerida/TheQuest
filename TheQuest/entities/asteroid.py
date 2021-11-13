import os
import pygame as pg
from pygame.sprite import Sprite
from random import randint

from TheQuest import AS_SPEED_X_FINISH, IMAGES, RESOURCES, SC_HEIGHT, SC_WIDTH


class Asteroid(Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'asteroids', f'asteroid_{randint(1,10)}.png'))
        self.dodged = False
        self.rect = self.image.get_rect()
        self.level = level
        self.create_asteroid()
        self.speed_x = randint(self.level, self.level+1)

    def create_asteroid(self):
        x = randint(SC_WIDTH, SC_WIDTH+100)
        y = randint(0, SC_HEIGHT)
        self.rect.midleft = (x, y)

    def update(self, to_end=False, *args, **kwargs):
        if to_end:
            self.rect.x -= AS_SPEED_X_FINISH
        else:
            self.rect.x -= self.speed_x
        if self.rect.right < 0:
            self.dodged = True

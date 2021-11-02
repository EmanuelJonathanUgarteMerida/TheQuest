import pygame as pg
import os

from pygame.sprite import Sprite

from TheQuest import SC_HEIGHT, SS_BONUS_LEVEL, SS_LIFE_LIMIT, RESOURCES, SS_IMG_NAME, SS_IMG_SIZE, SS_SPEED_Y


class SpaceShip(Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            RESOURCES, 'images', SS_IMG_NAME))
        self.score = 0
        self.lives = SS_LIFE_LIMIT
        self.level = 0
        self.name = name
        self.speed_y = SS_SPEED_Y
        self.sound_explosion = ''
        self.initialize()

    def initialize(self):
        self.image = pg.transform.scale(self.image, SS_IMG_SIZE)
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            self.rect.top -= self.speed_y
        elif pressed[pg.K_DOWN]:
            self.rect.bottom += self.speed_y

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SC_HEIGHT:
            self.rect.bottom = SC_HEIGHT

    def level_up(self):
        self.speed_y += 1
        self.lives += 1
        self.score += SS_BONUS_LEVEL
        # cambia imagen al subir level

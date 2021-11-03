import os
from random import randint
import pygame as pg
from pygame.sprite import Sprite
from TheQuest import BO_OBJECTS, RESOURCES, SC_HEIGHT, SC_WIDTH


class BoxObject(Sprite):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.box = BO_OBJECTS[randint(0, len(BO_OBJECTS)-1)]
        self.image_name = self.box[1][0]
        self.image = pg.image.load(os.path.join(
            RESOURCES, 'images', 'bonus_items', self.image_name)).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        x = randint(100, SC_WIDTH)
        y = randint(0, SC_HEIGHT)
        self.rect.center = (x, y)
        self.speed_x = randint(1, 3)

    def update(self, *args, **kwargs):
        self.rect.x -= self.speed_x

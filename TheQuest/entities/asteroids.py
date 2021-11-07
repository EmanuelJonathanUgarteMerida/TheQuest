import json
from random import randint
from TheQuest import AS_PATH_IMG, AS_PATH_JSON
import pygame as pg

from TheQuest.entities.asteroid import Asteroid


class Asteroids():
    def __init__(self):
        self.sprite_sheet = pg.image.load(AS_PATH_IMG).convert_alpha()
        self.colorkey = (0, 0, 0)
        self.group = pg.sprite.Group()

    def generate_asteroid(self, total):
        json_data = open(AS_PATH_JSON, 'r')
        d = json.load(json_data)
        json_data.close()

        for x in range(total):
            i = randint(1, 4)
            im = d[f'{i}']
            ast = self.get_image(im, 1)
            self.group.add(Asteroid(ast))

    def get_image(self, settings, scale):
        width = settings['width']
        height = settings['height']
        x = settings['x']
        y = settings['y']
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(self.colorkey)
        return image

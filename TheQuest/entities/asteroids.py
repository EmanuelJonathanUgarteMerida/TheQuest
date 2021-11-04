import json
from random import randint
from TheQuest import AS_PATH_JSON
import pygame as pg


class Asteroids():
    def __init__(self, size):
        self.size = size
        self.asteroids = []

    def generate_asteroid(self):
        json_data = open(AS_PATH_JSON, 'r')
        d = json.load(json_data)
        json_data.close()

        for x in range(5):
            i = randint(0, 3)
            im = d[f'{i}']
            ast = self.get_image(im, 1)
            # asteroids_group.add(ast)

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

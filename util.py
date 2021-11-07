import os
import pygame as pg
import json

from TheQuest import IMAGES, RESOURCES


class SpriteSheet():
    def __init__(self, img_name, json_name, colorkey):
        self.sprite_sheet = pg.image.load(os.path.join(
            RESOURCES, IMAGES, img_name)).convert_alpha()
        self.leer_json(json_name)
        self.colorkey = colorkey
        self.images = []
        self.get_image_compose()

    def leer_json(self, file):
        json_data = open(os.path.join(RESOURCES, IMAGES, file), 'r')
        self.data = json.load(json_data)
        json_data.close()

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

    def get_image_compose(self):
        for row in self.data:
            self.images.append(self.get_image(self.data[row], 1))

import pygame as pg
import json
import os

from TheQuest import RESOURCES


class SpriteSheet():
    def __init__(self, name_img, name_json, colorkey):
        self.sprite_sheet = pg.image.load(
            os.path.join(RESOURCES, 'images', name_img)).convert_alpha()
        self.data = self.leer_json(name_json)
        self.colorkey = colorkey

    def leer_json(self, file_name):
        json_data = open(os.path.join(RESOURCES, 'images', file_name), 'r')
        d = json.load(json_data)
        json_data.close()
        return d

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
        return

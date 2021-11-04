import pygame as pg
import json

from TheQuest import AS_PATH_IMG, AS_PATH_JSON


class SpriteSheet():
    def __init__(self, colorkey):
        self.sprite_sheet = pg.image.load(AS_PATH_IMG).convert_alpha()
        self.data = self.leer_json()
        self.colorkey = colorkey

    def leer_json(self):
        json_data = open(AS_PATH_JSON, 'r')
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

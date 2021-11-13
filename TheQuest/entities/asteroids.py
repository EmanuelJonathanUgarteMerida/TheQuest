import pygame as pg

from TheQuest.entities.asteroid import Asteroid


class Asteroids():
    def __init__(self, level=1):
        self.colorkey = (0, 0, 0)
        self.level = level
        self.group = pg.sprite.Group()

    def generate_asteroid(self, total):
        count = 0
        while count < total:
            self.group.add(Asteroid(self.level))
            count += 1

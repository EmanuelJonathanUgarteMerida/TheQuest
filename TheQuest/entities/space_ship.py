import pygame as pg
import os

from TheQuest import IMG_NAME, IMG_SIZE, RESOURCES
class SpaceShip():
    def __init__(self):
        self.image=pg.image.load(os.path.join(RESOURCES,'images',IMG_NAME))
        self.image=pg.transform.scale(self.image,IMG_SIZE)
        self.score=0
        self.lifes=0
        self.level=0
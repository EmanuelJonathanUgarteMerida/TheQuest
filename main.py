import pygame as pg

from TheQuest import G_PATH_IMG, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.level import Level

pg.init()
pg.mixer.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
bg = pg.image.load(G_PATH_IMG)

level = Level(screen, clock, bg, 1, 'Jhon')
level.play()

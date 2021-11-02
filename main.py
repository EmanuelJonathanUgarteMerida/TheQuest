import pygame as pg

import os

from TheQuest import FPS, HEIGHT_SC, RESOURCES, WIDTH_SC
from TheQuest.entities.space_ship import SpaceShip

clock=pg.time.Clock()
screen=pg.display.set_mode((WIDTH_SC,HEIGHT_SC))
bg=pg.image.load(os.path.join(RESOURCES,'images','background','space_1.jpg'))
bg_rect =bg.get_rect()
space_ship=SpaceShip()
game_over=False
frames=0
while not game_over:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_over=True
    if frames == 2:
        bg_rect.x-=1
        frames=0
    frames+=1
    screen.blit(bg,bg_rect)
    screen.blit(space_ship.image,space_ship.image.get_rect())
    pg.display.flip()
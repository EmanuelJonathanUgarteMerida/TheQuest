import pygame as pg

import os

from TheQuest import FPS, RESOURCES, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.space_ship import SpaceShip

clock = pg.time.Clock()
screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
bg = pg.image.load(os.path.join(
    RESOURCES, 'images', 'background', 'space_1.jpg'))
bg_rect = bg.get_rect()
player = SpaceShip('Jonathan')
game_over = False
frames = 0

#sprite_groups = pg.sprite.Group()
# sprite_groups.add(space_ship)

while not game_over:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_over = True
    if frames == 2:
        bg_rect.x -= 1
        frames = 0
    frames += 1

    player.update()

    screen.blit(bg, bg_rect)
    screen.blit(player.image, player.rect)
    pg.display.flip()

import pygame as pg

import os
from random import randint
from pygame.image import load

from TheQuest import FPS, RESOURCES, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.box_object import BoxObject
from TheQuest.entities.space_ship import SpaceShip
from TheQuest.entities.asteroid import Asteroid
from util import SpriteSheet

pg.init()
pg.mixer.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
bg = pg.image.load(os.path.join(
    RESOURCES, 'images', 'background', 'space_1.jpg'))
bg_rect = bg.get_rect()

# we created our asteroids
asteroid_sheet = SpriteSheet(
    'asteroids_sheet.png', 'asteroids_sheet.json', (255, 250, 205))
asteroids_group = pg.sprite.Group()
for x in range(25):
    i = randint(0, 3)
    im = asteroid_sheet.data[f'{i}']
    ast = Asteroid(asteroid_sheet.get_image(im, 1))
    asteroids_group.add(ast)

# BoxObject
box = BoxObject()
boxes_group = pg.sprite.Group()
boxes_group.add(box)

# we created our space ship
player = SpaceShip('Jonathan')

game_over = False
frames = 0

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
    asteroids_group.update()
    boxes_group.update()

    player.collision_asteroids(asteroids_group)
    player.collision_boxes(boxes_group)

    screen.blit(bg, bg_rect)
    asteroids_group.draw(screen)
    boxes_group.draw(screen)
    screen.blit(player.image, player.rect)
    pg.display.flip()

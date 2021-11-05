import pygame as pg

import os
from random import randint
from pygame.image import load

from TheQuest import FPS, G_PATH_IMG, RESOURCES, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.box_object import BoxObject
from TheQuest.entities.scoreboard import ScoreBoard
from TheQuest.entities.space_ship import SpaceShip
from TheQuest.entities.asteroid import Asteroid
from util import SpriteSheet

pg.init()
pg.mixer.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
bg = pg.image.load(G_PATH_IMG)
bg_rect = bg.get_rect()

score_board = ScoreBoard()

# we created our asteroids
asteroid_sheet = SpriteSheet((255, 250, 205))
asteroids_group = pg.sprite.Group()

asteroides = Asteroids(8)

for x in range(5):
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


def updates():
    player.update()
    asteroides.group.update(player)
    boxes_group.update()
    score_board.update(player.score, player.lives, 0, 120)


def collisions():
    player.collision_asteroids(asteroides.group)
    player.collision_boxes(boxes_group)


def blits():
    screen.blit(bg, bg_rect)
    screen.blit(player.image, player.rect)
    screen.blit(score_board.score_player, score_board.score_player_rect)
    screen.blit(score_board.lives_player, score_board.lives_player_rect)
    screen.blit(score_board.level_game, score_board.level_game_rect)
    screen.blit(score_board.time_game, score_board.time_game_rect)


def draws():
    asteroides.group.draw(screen)
    boxes_group.draw(screen)


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

    updates()
    collisions()
    blits()
    draws()

    pg.display.flip()

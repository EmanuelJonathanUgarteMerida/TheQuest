from random import randint
from TheQuest import FPS, G_LEVEL_LIMIT_TIME
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.box_object import BoxObject
from TheQuest.entities.planet import Planet
from TheQuest.entities.scoreboard import ScoreBoard
from TheQuest.entities.space_ship import SpaceShip
import pygame as pg


class Level():
    def __init__(self, screen, clock, bg, level, player_name):
        self.screen = screen
        self.clock = clock
        self.game_over = False
        self.level = level
        self.level_completed = False
        self.image_bg = bg
        self.image_bg_rect = self.image_bg.get_rect()
        self.bg_sound = 0
        self.timer = 0
        # classes
        self.planet = Planet(str(self.level))
        self.score_board = ScoreBoard()
        self.asteroids = Asteroids()
        self.player = SpaceShip(player_name)
        self.segundos = 0

    def updates(self):
        ticks = pg.time.get_ticks()//1000
        self.planet.update()
        if self.segundos >= G_LEVEL_LIMIT_TIME:
            #self.planet.update()
            self.level_completed = True
            self.player.auto = True
        elif ticks > self.segundos:
            self.asteroids.generate_asteroid(randint(1, 3))
            self.segundos = ticks

        self.player.update()
        self.asteroids.group.update(self.player)

        self.score_board.update(
            self.player.score, self.player.lives, 0, self.segundos)
        self.image_bg_rect.left -= 1

    def collisions(self):
        self.player.collision_asteroids(self.asteroids.group)

    def blits(self):
        self.screen.blit(self.image_bg, self.image_bg_rect)
        self.screen.blit(self.planet.image, self.planet.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.score_board.score_player,
                         self.score_board.score_player_rect)
        self.screen.blit(self.score_board.lives_player,
                         self.score_board.lives_player_rect)
        self.screen.blit(self.score_board.level_game,
                         self.score_board.level_game_rect)
        self.screen.blit(self.score_board.time_game,
                         self.score_board.time_game_rect)

    def draws(self):
        self.asteroids.group.draw(self.screen)

    def play(self):
        while not self.game_over:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.game_over = True
            self.updates()
            self.collisions()
            self.blits()
            self.draws()
            pg.display.flip()

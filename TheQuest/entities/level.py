from random import randint
from TheQuest import FPS, G_LEVEL_LIMIT_TIME
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.box_object import BoxObject
from TheQuest.entities.planet import Planet
from TheQuest.entities.space_ship import SpaceShip
import pygame as pg


class Level():
    def __init__(self, screen, clock, level, info_card):
        self.screen = screen
        self.clock = clock
        self.game_over = False
        self.level = level
        self.level_completed = False
        self.bg_sound = 0
        self.timer = 0
        # classes
        self.planet = Planet(str(self.level))
        self.info_card = info_card
        self.asteroids = Asteroids()
        self.player = SpaceShip()
        self.reset_ship = False

    def updates(self):
        ticks = pg.time.get_ticks()//1000
        if self.info_card.time >= G_LEVEL_LIMIT_TIME:
            self.planet.update()
            self.level_completed = True
            self.player.auto = True
        elif ticks > self.info_card.time:
            self.asteroids.generate_asteroid(randint(1, 3))

        self.info_card.time = ticks
        self.player.update()
        self.asteroids.group.update()
        self.info_card.update()

        for sprite in self.asteroids.group:
            if sprite.dodged:
                self.info_card.score += 1
                sprite.kill()
                # print(self.info_card.score)

    def collisions(self):
        self.player.collision_asteroids(self.asteroids.group)
        if self.player.collided:
            self.info_card.lives -= 1
            self.player = SpaceShip(pg.time.get_ticks()//1000)

    def blits(self):
        self.screen.blit(self.planet.image, self.planet.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.info_card.score_player,
                         self.info_card.score_player_rect)
        self.screen.blit(self.info_card.lives_player,
                         self.info_card.lives_player_rect)
        self.screen.blit(self.info_card.level_game,
                         self.info_card.level_game_rect)
        self.screen.blit(self.info_card.time_game,
                         self.info_card.time_game_rect)

    def draws(self):
        self.asteroids.group.draw(self.screen)

    def start(self):
        while not self.game_over:
            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.game_over = True
            self.updates()
            self.collisions()
            self.blits()
            self.draws()
            pg.display.flip()

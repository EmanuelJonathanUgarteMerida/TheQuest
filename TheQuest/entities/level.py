import os
from random import randint

from pygame.transform import rotate
from TheQuest import FPS, G_LEVEL_LIMIT_TIME, IMAGES, RESOURCES, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.planet import Planet
from TheQuest.entities.space_ship import SpaceShip
import pygame as pg


class Level():
    def __init__(self, screen, clock, level, info_card):
        self.screen = screen
        self.clock = clock
        self.level = level
        self.info_card = info_card
        self.info_card.level = level
        self.info_card.time = G_LEVEL_LIMIT_TIME
        self.load_background()
        self.game_over = False
        self.frame = 0
        self.frame_sec = 0
        self.planet = Planet(self.level)
        self.asteroids = Asteroids(self.level)
        self.player = SpaceShip(self.level)
        self.angle = 0

    def load_background(self):
        self.bg = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'background', f'bg_{self.level}.jpg'))
        self.bg_rect = self.bg.get_rect()

    def updates(self):
        self.frame_sec += 1
        if self.info_card.time == 0:
            self.planet.update()
            self.player.auto = True
        elif self.frame_sec == 60 and self.info_card.lives >= 0:
            self.info_card.time -= 1
            self.frame_sec = 0
            self.asteroids.generate_asteroid(randint(self.level, self.level+1))

        self.player.update()
        if self.player.landed:
            self.info_card.score += self.planet.bonus_points
            self.planet.bonus_points = 0

        if self.player.auto:
            self.asteroids.group.update(True)
        else:
            self.asteroids.group.update()
        self.info_card.update(self.player.landed)

        for sprite in self.asteroids.group:
            if sprite.dodged:
                self.info_card.score += 1
                sprite.kill()

        if self.frame == 1:
            self.bg_rect.left -= 1
            self.frame = 0
        else:
            self.frame += 1

    def collisions(self):
        if self.player.collided:
            if not self.player.collide_animation:
                self.info_card.lives -= 1
                if self.info_card.lives >= 0:
                    self.player = SpaceShip(self.level)
        else:
            self.player.collision_asteroids(self.asteroids.group)

    def blits(self):
        self.screen.blit(self.planet.image, self.planet.rect)
        if self.player.landed:
            img_copy = pg.transform.rotate(
                self.player.image, self.player.angle)
            x, y = self.player.rect.center
            self.screen.blit(
                img_copy, (x-int(img_copy.get_width()/2), y-int(img_copy.get_height()/2)))
            print(f'rotando {self.player.angle}')
        else:
            self.screen.blit(self.player.image, self.player.rect)

    def blit_info(self):
        self.screen.blit(self.info_card.score_player,
                         self.info_card.score_player_rect)

        if not self.info_card.lives < 0:
            self.screen.blit(self.info_card.lives_player,
                             self.info_card.lives_player_rect)

        self.screen.blit(self.info_card.level_game,
                         self.info_card.level_game_rect)

        self.screen.blit(self.info_card.time_game,
                         self.info_card.time_game_rect)

        if self.player.landed:
            self.screen.blit(self.info_card.level_completed,
                             self.info_card.level_completed_rect)
            self.screen.blit(self.info_card.continued,
                             self.info_card.continued_rect)

        if self.info_card.lives < 0:
            # Termina partida, mantener pantalla y preguntar si reiniciar o salir, salir llevará a pantalla inicio
            # Se guarda la informacion en el ranking del juego
            print('Sin vidas!')

    def draws(self):
        self.asteroids.group.draw(self.screen)

    def loop_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game_over = True
                if self.player.landed and event.key == pg.K_SPACE:
                    self.game_over = True

    def start(self):
        while not self.game_over:
            self.clock.tick(FPS)

            self.loop_events()

            self.updates()

            self.screen.blit(self.bg, self.bg_rect)

            self.collisions()
            self.draws()
            self.blits()
            self.blit_info()
            pg.display.update()

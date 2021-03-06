import os
from random import randint

from pygame.transform import rotate
from TheQuest import BACKGROUND, FPS, G_MAX_LEVEL, G_REMAINING_TIME, IMAGES, RESOURCES, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SC_HEIGHT, SC_WIDTH, SOUNDS
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.planet import Planet
from TheQuest.entities.space_ship import SpaceShip
import pygame as pg

from utils import create_text


class Level():
    def __init__(self, screen, clock, level, info_card, database):
        self.screen = screen
        self.clock = clock
        self.level = level
        self.info_card = info_card
        self.database = database
        self.load_background()
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 80)
        self.font_rank = pg.font.Font(SB_PATH_FONT_BOARD, 20)
        self.still = True
        self.restart = False
        self.frame = 0
        self.frame_sec = 0
        self.planet = Planet(self.level)
        self.asteroids = Asteroids(self.level)
        self.player = SpaceShip(self.level)
        self.countdown = G_REMAINING_TIME
        self.user_text = ''
        self.verificated_bbdd = False
        self.min_score = 0
        self.show_ranking = False
        self.best_players = []
        self.i = 0

    def load_background(self):
        self.bg = pg.image.load(os.path.join(
            RESOURCES, IMAGES, BACKGROUND, f'bg_{self.level}.jpg'))
        self.bg_rect = self.bg.get_rect()

    def updates(self):
        self.frame_sec += 1
        if self.info_card.time == 0:
            self.planet.update()
            self.player.auto = True
        elif self.frame_sec == FPS and self.info_card.lives > 0:
            self.info_card.time -= 1
            self.frame_sec = 0
            print('Se genera asteroides')
            self.asteroids.generate_asteroid(randint(self.level, self.level+1))

        self.player.update()
        self.player.bullets.update()

        if self.player.landed:
            self.info_card.score += self.planet.bonus_points
            self.planet.bonus_points = 0
            self.info_card.game_completed = self.level == G_MAX_LEVEL
            self.info_card.landed = True

        self.asteroids.group.update(self.player.auto)
        self.info_card.update()

        self.verify_asteroid_dodged()

        if self.frame == 1:
            self.bg_rect.left -= 1
            self.frame = 0
        else:
            self.frame += 1

    def verify_asteroid_dodged(self):
        for sprite in self.asteroids.group:
            if sprite.dodged:
                self.info_card.score += 1
                sprite.kill()

    def collisions(self):
        if self.player.collided:
            if not self.player.collide_animation:
                self.info_card.lives -= 1
                if self.info_card.lives > 0:
                    self.player = SpaceShip(self.level)
                else:
                    self.info_card.update()
        else:
            self.player.collision_asteroids(self.asteroids.group)
            collisions = pg.sprite.groupcollide(
                self.player.bullets, self.asteroids.group, True, True)
            if len(collisions) > 0:
                self.info_card.score += 1
                pg.mixer.Sound(os.path.join(
                    RESOURCES, SOUNDS, 'bom.mp3')).play()

    def blits(self):
        self.screen.blit(self.planet.image, self.planet.rect)
        if self.player.landed:
            self.rotate_rocket()
        else:
            self.screen.blit(self.player.image, self.player.rect)

    def rotate_rocket(self):
        img_copy = pg.transform.rotate(
            self.player.image, self.player.angle)
        x, y = self.player.rect.center
        self.screen.blit(
            img_copy, (x-int(img_copy.get_width()/2), y-int(img_copy.get_height()/2)))

    def blit_info(self):
        self.blit_stats('score')
        self.blit_stats('lives')
        self.blit_stats('level')
        self.blit_stats('time')

        if self.info_card.lives == 0:
            self.blit_message('game_over')
            self.countdown_blit()
            self.blit_message('restart')

        elif self.player.landed:
            if self.info_card.game_completed:
                self.blit_message('final')
                if self.show_ranking:
                    self.load_ranking()
                else:
                    self.between_min_score()
                    if self.info_card.score > self.min_score:
                        self.blit_message('initials')
                        input_txt = create_text(
                            self.font, self.user_text, 'center', (SC_WIDTH/2, SC_HEIGHT/2))
                        self.screen.blit(input_txt[0], input_txt[1])
                    self.blit_message('save')
                self.blit_message('restart')
            else:
                self.blit_message('level_completed')
                self.blit_message('continued')

    def blit_message(self, key):
        render = self.info_card.messages[key]
        self.screen.blit(render[0], render[1])

    def blit_stats(self, key):
        render = self.info_card.stats[key]
        self.screen.blit(render[0], render[1])

    def blit_players(self, player, distance):
        nick = player[0]
        score = player[1]
        render = create_text(
            self.font_rank, f'{nick} --- \t{score}', 'midbottom', (SC_WIDTH/2, SC_HEIGHT/2-50+distance))
        self.screen.blit(render[0], render[1])

    def load_ranking(self):
        distance = 0
        for player in self.best_players:
            self.blit_players(player, distance)
            distance += 20

    def between_min_score(self):
        if not self.verificated_bbdd:
            self.min_score = self.database.select_min_score()
            self.verificated_bbdd = True

    def countdown_blit(self):
        if self.frame_sec == 60:
            self.countdown -= 1
            self.frame_sec = 0
        else:
            self.frame_sec += 1

        if self.countdown >= 0:
            count_down = create_text(
                self.font, self.countdown, 'center', (SC_WIDTH/2, SC_HEIGHT/2))
            self.screen.blit(count_down[0], count_down[1])

    def draws(self):
        self.asteroids.group.draw(self.screen)
        self.player.bullets.draw(self.screen)

    def create_bg_close_level(self):
        if self.info_card.lives == 0 or self.player.landed:
            self.screen.blit(self.info_card.shadow, self.info_card.shadow_rect)

    def save_or_update_score(self):
        self.database.save_or_update_info(
            self.user_text, self.info_card.score, self.level)

    def loop_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if self.player.landed and self.info_card.game_completed:
                    if event.key == pg.K_BACKSPACE:
                        if len(self.user_text) > 0:
                            self.user_text = self.user_text[:-1]
                    elif event.key in (pg.K_KP_ENTER, pg.K_RETURN):
                        if len(self.user_text) > 0:
                            self.save_or_update_score()
                            self.best_players.clear()
                            self.best_players = self.database.select_best_players()
                            self.show_ranking = True
                    elif len(self.user_text) < 3:
                        self.user_text += event.unicode

                if event.key == pg.K_SPACE:
                    if self.player.landed:
                        self.still = False
                    elif self.info_card.lives == 0 or self.info_card.game_completed:
                        self.still = False
                        self.restart = True
            elif event.type == pg.KEYUP:
                self.player.frame_state = self.player.frame_to_shoot

    def blit_background(self):
        self.screen.blit(self.bg, (self.i, 0))
        self.screen.blit(self.bg, (self.bg.get_width()+self.i, 0))
        if (self.i == -self.bg.get_width()):
            self.screen.blit(self.bg, (self.bg.get_width()+self.i, 0))
            self.i = 0
        self.i -= 1

    def start(self):
        while self.still:
            self.clock.tick(FPS)

            self.loop_events()

            if self.info_card.lives > 0:
                self.collisions()

            self.screen.blit(self.bg, self.bg_rect)

            self.blit_background()

            if self.info_card.lives > 0:
                self.updates()

            if self.countdown < 0:
                self.info_card.afk = True
                self.still = False
            self.draws()
            self.create_bg_close_level()
            self.blits()
            self.blit_info()
            pg.display.flip()

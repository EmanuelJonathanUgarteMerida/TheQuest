
import os
from random import randint

from pygame.display import Info
from TheQuest import FPS, G_LEVEL_LIMIT_TIME, PR_DESC, PR_PATH_BG, PR_PATH_IMG_DOWN, PR_PATH_IMG_UP, RESOURCES, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SC_HEIGHT, SC_WIDTH
from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.info_card import InfoCard
from TheQuest.entities.level import Level
import pygame as pg


class Scene:
    def __init__(self, screen, clock, info_card, database):
        self.screen = screen
        self.clock = clock
        self.info_card = info_card
        self.database = database

    def start(self):
        pass


class Presentation(Scene):
    def __init__(self, screen, clock, info_card, database):
        super().__init__(screen, clock, info_card, database)
        self.clock = clock
        self.bg = pg.image.load(PR_PATH_BG)
        self.bg = pg.transform.scale(self.bg, (SC_WIDTH, SC_HEIGHT))
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)
        self.load_images()
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 50)

        self.title = self.font.render('The Quest', True, SB_COLOR_BOARD_TEXT)
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = (SC_WIDTH/2, 100)

        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 20)
        self.up_text = self.font.render(
            'Esquivar hacia arriba', True, SB_COLOR_BOARD_TEXT)
        self.up_text_rect = self.up_text.get_rect()
        self.up_text_rect.midleft = (
            SC_WIDTH/2-25, SC_HEIGHT/2-self.up.get_height()/2+50)

        self.down_text = self.font.render(
            'Esquivar hacia abajo', True, SB_COLOR_BOARD_TEXT)
        self.down_text_rect = self.down_text.get_rect()
        self.down_text_rect.midleft = (
            SC_WIDTH/2-25, SC_HEIGHT/2+self.up.get_height()/2+50)

        self.to_play = self.font.render(
            'Preciona <Espacio> para iniciar', True, SB_COLOR_BOARD_TEXT)
        self.to_play_rect = self.to_play.get_rect()
        self.to_play_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-200)

        self.stay_here = True

    def create_descripcion(self):
        distance = 0
        for txt in PR_DESC:
            text = self.info_card.render(txt)
            text_rect = text.get_rect()
            text_rect.midtop = (SC_WIDTH/2, 180+distance)
            self.screen.blit(text, text_rect)
            distance += 20

    def load_images(self):
        self.up = pg.image.load(PR_PATH_IMG_UP)
        self.up_rect = self.up.get_rect()
        self.up_rect.bottomright = (SC_WIDTH/2-50, SC_HEIGHT/2+50)

        self.down = pg.image.load(PR_PATH_IMG_DOWN)
        self.down_rect = self.down.get_rect()
        self.down_rect.topright = (SC_WIDTH/2-50, SC_HEIGHT/2+50)

    def start(self):
        while self.stay_here:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.stay_here = False

            self.screen.blit(self.bg, self.bg_rect)
            self.screen.blit(self.title, self.title_rect)
            self.create_descripcion()
            self.screen.blit(self.up, self.up_rect)
            self.screen.blit(self.down, self.down_rect)
            self.screen.blit(self.up_text, self.up_text_rect)
            self.screen.blit(self.down_text, self.down_text_rect)
            self.screen.blit(self.to_play, self.to_play_rect)

            pg.display.flip()


class Quest (Scene):
    def __init__(self, screen, clock, info_card, database):
        super().__init__(screen, clock, info_card, database)
        self.database = database
        self.levels = 7

    def start(self):
        number_level = 1
        while number_level <= self.levels:
            self.info_card.level = number_level
            self.info_card.time = G_LEVEL_LIMIT_TIME
            self.info_card.load_default_messages()
            level = Level(self.screen, self.clock,
                          number_level, self.info_card, self.database)
            print(
                f'\n\n############## LEVEL {level.level} Creado ##############')
            level.start()

            if self.info_card.lives == 0 or self.info_card.game_completed:
                if level.info_card.afk:
                    number_level = 99
                else:
                    self.info_card = InfoCard()
                    number_level = 1
            else:
                number_level += 1

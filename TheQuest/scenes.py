
import os
from random import randint

from pygame.display import Info
from TheQuest import FPS, PR_DESC, PR_PATH_BG, RESOURCES, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SC_HEIGHT, SC_WIDTH
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
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 50)

        self.title = self.font.render('The Quest', True, SB_COLOR_BOARD_TEXT)
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = (SC_WIDTH/2, 100)

        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 20)
        self.desc = self.font.render(PR_DESC, True, SB_COLOR_BOARD_TEXT)
        self.desc_rect = self.desc.get_rect()
        self.desc_rect.midtop = (SC_WIDTH/2, 180)

        self.to_play = self.font.render(
            'Preciona <Espacio> para iniciar', True, SB_COLOR_BOARD_TEXT)
        self.to_play_rect = self.to_play.get_rect()
        self.to_play_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-200)

        self.stay_here = True

    def start(self):
        while self.stay_here:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.stay_here = False

            self.screen.blit(self.bg, self.bg_rect)
            self.screen.blit(self.title, self.title_rect)
            self.screen.blit(self.desc, self.desc_rect)
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
            level = Level(self.screen, self.clock,
                          number_level, self.info_card)
            level.start()

            if self.info_card.lose or self.info_card.game_completed:
                self.database.insert_update_info(
                    'WEY', self.info_card.score, number_level)
                self.info_card = InfoCard()
                number_level = 1
            else:
                number_level += 1


import os
from random import randint

from pygame.display import Info
from TheQuest import FPS, PR_DESC, PR_PATH_BG, PR_PATH_IMG_DOWN, PR_PATH_IMG_UP, RESOURCES, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SC_HEIGHT, SC_WIDTH
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
        self.load_images()
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 50)
        self.ranked = False

        self.title = self.font.render('The Quest', True, SB_COLOR_BOARD_TEXT)
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = (SC_WIDTH/2, 100)

        self.font = pg.font.Font(SB_PATH_FONT_BOARD, 20)
        self.desc = self.font.render(PR_DESC, True, SB_COLOR_BOARD_TEXT)
        self.desc_rect = self.desc.get_rect()
        self.desc_rect.midtop = (SC_WIDTH/2, 180)

        self.up_text = self.font.render(
            'Esquivar hacia arriba', True, SB_COLOR_BOARD_TEXT)
        self.up_text_rect = self.up_text.get_rect()
        self.up_text_rect.midleft = (
            SC_WIDTH/2, SC_HEIGHT/2-self.up.get_height()/2)

        self.down_text = self.font.render(
            'Esquivar hacia abajo', True, SB_COLOR_BOARD_TEXT)
        self.down_text_rect = self.down_text.get_rect()
        self.down_text_rect.topleft = (
            SC_WIDTH/2, SC_HEIGHT/2+self.up.get_height()/2)

        self.to_play = self.font.render(
            'Preciona <Espacio> para iniciar', True, SB_COLOR_BOARD_TEXT)
        self.to_play_rect = self.to_play.get_rect()
        self.to_play_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-200)

        self.to_ranking = self.font.render(
            'Preciona <Enter> para ver Ranking', True, SB_COLOR_BOARD_TEXT)
        self.to_ranking_rect = self.to_ranking.get_rect()
        self.to_ranking_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-100)

        self.stay_here = True

    def load_images(self):
        self.up = pg.image.load(PR_PATH_IMG_UP)
        self.up_rect = self.up.get_rect()
        self.up_rect.bottomright = (SC_WIDTH/2, SC_HEIGHT/2)

        self.down = pg.image.load(PR_PATH_IMG_DOWN)
        self.down_rect = self.down.get_rect()
        self.down_rect.topright = (SC_WIDTH/2, SC_HEIGHT/2)

    def start(self):
        while self.stay_here:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.stay_here = False
                    elif event.key == pg.K_KP_ENTER:
                        self.ranked = True
                        self.stay_here = False

            self.screen.blit(self.bg, self.bg_rect)
            self.screen.blit(self.title, self.title_rect)
            self.screen.blit(self.desc, self.desc_rect)
            self.screen.blit(self.up, self.up_rect)
            self.screen.blit(self.down, self.down_rect)
            self.screen.blit(self.up_text, self.up_text_rect)
            self.screen.blit(self.down_text, self.down_text_rect)
            self.screen.blit(self.to_play, self.to_play_rect)
            self.screen.blit(self.to_ranking, self.to_ranking_rect)

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
                if level.info_card.afk:
                    print('Terminamos partida')
                    number_level = 99
                else:
                    self.info_card = InfoCard()
                    number_level = 1
            else:
                number_level += 1


class Ranking (Scene):
    def __init__(self, screen, clock, info_card, database):
        super().__init__(screen, clock, info_card, database)
        self.font = self.font = pg.font.Font(SB_PATH_FONT_BOARD, 50)

        self.rank = self.font.render(
            'Los 5 mejores jugadores', True, SB_COLOR_BOARD_TEXT)
        self.rank_rect = self.rank.get_rect()
        self.rank_rect.midtop = (SC_WIDTH/2, 20)

        self.best_players = database.select_best_players()
        self.still = True
        self.players_txt = []
        self.load_players()

    def load_players(self):
        distance = 0
        for row in self.best_players:
            distance += 50
            self.players_txt.append(self.blit_players(row, distance))

    def blit_players(self, row, distance):
        nick = row[0]
        score = row[1]
        player = self.font.render(
            f'{nick} --- \t{score}', True, SB_COLOR_BOARD_TEXT)
        player_rect = player.get_rect()
        player_rect.midtop = (SC_WIDTH/2, 100+distance)
        return (player, player_rect)

    def start(self):
        while self.still:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pg.quit()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.rank, self.rank_rect)
            for player in self.players_txt:
                self.screen.blit(player[0], player[1])
            pg.display.flip()

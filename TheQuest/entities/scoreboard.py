import pygame as pg

from TheQuest import SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SB_POS_LEVEL_GAME, SB_POS_LIVES_PLAYER, SB_POS_SCORE_PLAYER, SB_POS_TIME_GAME, SB_SIZE_BOARD_TEXT


class ScoreBoard():
    def __init__(self, name):
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, SB_SIZE_BOARD_TEXT)
        self.color_text = SB_COLOR_BOARD_TEXT
        self.anti_al = True
        self.score = 0
        self.lives = 0
        self.level = 0
        self.time = 0
        self.name = name

    def update(self):
        self.score_player = self.render(str(self.score))
        self.score_player_rect = self.score_player.get_rect()
        self.score_player_rect.topleft = SB_POS_SCORE_PLAYER

        self.lives_player = self.render(str(self.lives))
        self.lives_player_rect = self.lives_player.get_rect()
        self.lives_player_rect.topleft = SB_POS_LIVES_PLAYER

        self.level_game = self.render(str(self.level))
        self.level_game_rect = self.level_game.get_rect()
        self.level_game_rect.midtop = SB_POS_LEVEL_GAME

        self.time_game = self.render(str(self.time))
        self.time_game_rect = self.time_game.get_rect()
        self.time_game_rect.topright = SB_POS_TIME_GAME

    def render(self, txt):
        return self.font.render(txt, self.anti_al, self.color_text)

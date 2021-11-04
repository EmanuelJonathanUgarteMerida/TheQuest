import pygame as pg

from TheQuest import SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SB_SIZE_BOARD_TEXT


class ScoreBoard():
    def __init__(self):
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, SB_SIZE_BOARD_TEXT)
        self.color_text = SB_COLOR_BOARD_TEXT
        self.anti_al = True

    def update(self, score, lives, level_game, time):
        self.score_player = self.render(str(score))
        self.score_player_rect = self.score_player.get_rect()
        self.score_player_rect.topleft = (0, 0)

        self.lives_player = self.render(str(lives))
        self.lives_player_rect = self.lives_player.get_rect()
        self.lives_player_rect.center = (250, 250)

        self.level_game = self.render(str(level_game))
        self.level_game_rect = self.level_game.get_rect()
        self.level_game_rect.center = (300, 300)

        self.time_game = self.render(str(time))
        self.time_game_rect = self.time_game.get_rect()
        self.time_game_rect.center = (400, 400)

    def render(self, txt):
        return self.font.render(txt, self.anti_al, self.color_text)

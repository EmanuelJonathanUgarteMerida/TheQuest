import pygame as pg

from TheQuest import G_LEVEL_LIMIT_TIME, G_LIVES_LIMIT, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SB_POS_LEVEL_GAME, SB_POS_LIVES_PLAYER, SB_POS_SCORE_PLAYER, SB_POS_TIME_GAME, SB_SIZE_BOARD_TEXT, SC_HEIGHT, SC_WIDTH


class InfoCard():
    def __init__(self):
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, SB_SIZE_BOARD_TEXT)
        self.color_text = SB_COLOR_BOARD_TEXT
        self.anti_al = True
        self.landed = False
        self.game_completed = False
        self.lose = False
        self.time = G_LEVEL_LIMIT_TIME
        self.lives = G_LIVES_LIMIT
        self.level = 0
        self.score = 0

    def update(self):
        self.score_player = self.render(f'Puntos: {self.score}')
        self.score_player_rect = self.score_player.get_rect()
        self.score_player_rect.topleft = SB_POS_SCORE_PLAYER

        self.lives_player = self.render(f'Vidas: {self.lives}')
        self.lives_player_rect = self.lives_player.get_rect()
        self.lives_player_rect.midtop = SB_POS_LIVES_PLAYER

        self.level_game = self.render(f'Nivel: {self.level}')
        self.level_game_rect = self.level_game.get_rect()
        self.level_game_rect.midtop = SB_POS_LEVEL_GAME

        self.time_game = self.render(f'Tiempo: {self.time} s.')
        self.time_game_rect = self.time_game.get_rect()
        self.time_game_rect.topright = SB_POS_TIME_GAME

        if self.landed:
            if self.game_completed:
                self.final = self.render('Felicidades! Juego Terminado!')
                self.final_rect = self.final.get_rect()
                self.final_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)

            else:
                self.level_completed = self.render(
                    f'Nivel {self.level} Completado!')
                self.level_completed_rect = self.level_completed.get_rect()
                self.level_completed_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)

                self.continued = self.render(
                    'Presiona <ESPACIO> para continuar')
                self.continued_rect = self.continued.get_rect()
                self.continued_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-100)

        elif self.lose:
            self.game_over = self.render('Game Over...')
            self.game_over_rect = self.game_over.get_rect()
            self.game_over_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)

        if self.lose or self.game_completed:
            self.restart = self.render(
                'Presiona <Espacio> para reiniciar juego')
            self.restart_rect = self.restart.get_rect()
            self.restart_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT-100)

    def render(self, txt):
        return self.font.render(txt, self.anti_al, self.color_text)

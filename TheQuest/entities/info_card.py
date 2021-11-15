import pygame as pg

from TheQuest import G_LEVEL_LIMIT_TIME, G_LIVES_LIMIT, SB_COLOR_BOARD_TEXT, SB_PATH_FONT_BOARD, SB_POS_LEVEL_GAME, SB_POS_LIVES_PLAYER, SB_POS_SCORE_PLAYER, SB_POS_TIME_GAME, SB_SIZE_BOARD_TEXT, SC_HEIGHT, SC_WIDTH
from utils import create_text


class InfoCard():
    def __init__(self, level=0):
        self.font = pg.font.Font(SB_PATH_FONT_BOARD, SB_SIZE_BOARD_TEXT)
        self.color_text = SB_COLOR_BOARD_TEXT
        self.anti_al = True
        self.game_completed = False
        self.afk = False
        self.time = G_LEVEL_LIMIT_TIME
        self.lives = G_LIVES_LIMIT
        self.level = level
        self.score = 0
        self.load_shadow_box()

    def load_shadow_box(self):
        self.shadow = pg.Surface((SC_WIDTH/2, SC_HEIGHT/2),
                                 pg.SRCALPHA)
        self.shadow.fill((0, 0, 0, 150))
        self.shadow_rect = self.shadow.get_rect()
        self.shadow_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)

    def load_default_messages(self):

        self.messages = {}
        self.messages['final'] = create_text(
            self.font, 'Felicidades! Juego Terminado!', 'midbottom', (SC_WIDTH/2, SC_HEIGHT/2-100))
        self.messages['initials'] = create_text(
            self.font, 'Escribe 3 iniciales:', 'midtop', (SC_WIDTH/2, SC_HEIGHT/2-70))
        self.messages['level_completed'] = create_text(self.font, f'Nivel {self.level} Completado!', 'midbottom', (
            SC_WIDTH/2, SC_HEIGHT/2-50))
        self.messages['continued'] = create_text(
            self.font, 'Presiona <ESPACIO> para continuar', 'midtop', (SC_WIDTH/2, SC_HEIGHT/2+50))
        self.messages['game_over'] = create_text(
            self.font, 'Game Over...', 'midbottom', (SC_WIDTH/2, SC_HEIGHT/2-50))
        self.messages['restart'] = create_text(
            self.font, 'Presiona <Espacio> para reiniciar juego', 'midtop', (SC_WIDTH/2, SC_HEIGHT/2+100))
        self.messages['save'] = create_text(self.font, 'Presiona <Enter> para guardar puntos', 'midtop', (SC_WIDTH/2, SC_HEIGHT/2+50)
                                            )

        # Game Completed
        self.final = self.render('Felicidades! Juego Terminado!')
        self.final_rect = self.final.get_rect()
        self.final_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT/2-100)

        self.initials = self.render('Escribe 3 iniciales:')
        self.initials_rect = self.initials.get_rect()
        self.initials_rect.midtop = (SC_WIDTH/2, SC_HEIGHT/2-70)

        # Level Completed
        self.level_completed = self.render(
            f'Nivel {self.level} Completado!')
        self.level_completed_rect = self.level_completed.get_rect()
        self.level_completed_rect.midbottom = (
            SC_WIDTH/2, SC_HEIGHT/2-50)

        self.continued = self.render(
            'Presiona <ESPACIO> para continuar')
        self.continued_rect = self.continued.get_rect()
        self.continued_rect.midtop = (SC_WIDTH/2, SC_HEIGHT/2+50)

        # Game Over
        self.game_over = self.render('Game Over...')
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.midbottom = (SC_WIDTH/2, SC_HEIGHT/2-50)

        # Restart Game
        self.restart = self.render(
            'Presiona <Espacio> para reiniciar juego')
        self.restart_rect = self.restart.get_rect()
        self.restart_rect.midtop = (SC_WIDTH/2, SC_HEIGHT/2+100)

        self.guardar = self.render(
            'Presiona <Enter> para guardar puntos')
        self.guardar_rect = self.guardar.get_rect()
        self.guardar_rect.midtop = (SC_WIDTH/2, SC_HEIGHT/2+50)

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

    def render(self, txt):
        return self.font.render(txt, self.anti_al, self.color_text)

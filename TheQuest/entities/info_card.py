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
        self.messages = {}
        self.stats = {}

    def load_shadow_box(self):
        self.shadow = pg.Surface((SC_WIDTH/2, SC_HEIGHT/2),
                                 pg.SRCALPHA)
        self.shadow.fill((0, 0, 0, 150))
        self.shadow_rect = self.shadow.get_rect()
        self.shadow_rect.center = (SC_WIDTH/2, SC_HEIGHT/2)

    def load_default_messages(self):

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
        self.messages['save'] = create_text(
            self.font, 'Presiona <Enter> para guardar puntos', 'midtop', (SC_WIDTH/2, SC_HEIGHT/2+50))

    def update(self):
        self.stats['score'] = create_text(
            self.font, f'Puntos: {self.score}', 'topleft', SB_POS_SCORE_PLAYER)
        self.stats['lives'] = create_text(
            self.font, f'Vidas: {self.lives}', 'midtop', SB_POS_LIVES_PLAYER)
        self.stats['level'] = create_text(
            self.font, f'Nivel: {self.level}', 'midtop', SB_POS_LEVEL_GAME)
        self.stats['time'] = create_text(
            self.font, f'Tiempo: {self.time} s.', 'topright', SB_POS_TIME_GAME)

    def render(self, txt):
        return self.font.render(txt, self.anti_al, self.color_text)

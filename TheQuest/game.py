import pygame as pg
from pygame.constants import FULLSCREEN
from TheQuest import SC_HEIGHT, SC_WIDTH

from TheQuest.entities.info_card import InfoCard
from TheQuest.scenes import Presentation, Quest


class Game():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pg.time.Clock()
        self.info_card = InfoCard('jhon')
        # Cargamos las escenas Inicio - Partida - Fin Partida
        self.scenes = [Presentation(self.screen, self.clock, self.info_card), Quest(
            self.screen, self.clock, self.info_card)]

    def play(self):
        for scene in self.scenes:
            scene.start()
            if scene.info_card.lives == 0:
                print('perdiste el game papi!')
                pg.quit()

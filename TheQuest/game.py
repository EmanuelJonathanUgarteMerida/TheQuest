import pygame as pg
from pygame.constants import FULLSCREEN
from TheQuest import SC_HEIGHT, SC_WIDTH
from TheQuest.db_manager import DBManager

from TheQuest.entities.info_card import InfoCard
from TheQuest.scenes import Presentation, Quest, Ranking


class Game():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pg.time.Clock()
        self.scenes = []
        self.initialize()

    def initialize(self):
        self.info_card = InfoCard()
        self.database = DBManager()
        self.scenes.clear()
        self.scenes = [Presentation(self.screen, self.clock, self.info_card, self.database),
                       Quest(self.screen, self.clock,
                             self.info_card, self.database),
                       Ranking(self.screen, self.clock, self.info_card, self.database)]

    def play(self):
        index = 0
        while index < len(self.scenes):
            scene = self.scenes[index]
            scene.start()
            if index == 0:
                if scene.ranked:
                    self.scenes[2].start()

            if scene.info_card.afk:
                print('Volveremos a iniciar el juego')
                self.initialize()
                index = 0
            else:
                index += 1

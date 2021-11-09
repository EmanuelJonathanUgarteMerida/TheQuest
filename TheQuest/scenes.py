
from TheQuest import G_PATH_IMG
from TheQuest.entities.level import Level
import pygame as pg


class Scene:
    def __init__(self, screen, clock, info_card):
        self.screen = screen
        self.clock = clock
        self.info_card = info_card

    def start(self):
        pass


class Presentation(Scene):
    def __init__(self, screen, clock, info_card):
        super().__init__(screen, clock, info_card)

    def start(self):
        # aquí pedimos el nombre del jugador
        pass


class Quest (Scene):
    def __init__(self, screen, clock, info_card):
        super().__init__(screen, clock, info_card)
        self.levels = []
        self.init_levels()

    def init_levels(self):
        for x in range(1, 8):
            self.levels.append(
                Level(self.screen, self.clock, x, self.info_card))

    def start(self):
        for x in range(1, len(self.levels)+1):
            level = Level(self.screen, self.clock, x, self.info_card)
            level.start()
            # Comprobamos si se ha perdido las vidas para finalizar partida
            print(f'tenemos {self.info_card.lives} vidas')

from TheQuest.entities.asteroids import Asteroids
from TheQuest.entities.station import Station


class Level():
    def __init__(self, level, planet, bg, asteroids_total):
        self.level = level
        self.image_bg = bg
        self.asteroids = Asteroids(asteroids_total)
        self.image_planet = planet
        self.bg_sound = 0

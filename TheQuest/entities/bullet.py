import os
import pygame as pg
from pygame.sprite import Sprite

from TheQuest import SS_FREQ_ANIMATION, SS_PATH_IMG_BULLET


class Bullet(Sprite):
    def __init__(self, origin):
        super().__init__()
        self.images = []
        self.load_images()
        self.image = self.images[self.pos_img]
        self.rect = self.image.get_rect()
        self.rect.midright = origin
        self.freq_animation = 2
        self.pos_img = 0

    def load_images(self):
        self.images.clear()
        for x in range(1, 6):
            img = self.load_image(x)
            self.images.append(img)
        self.pos_img = 0

    def load_image(self, n):
        img_name = f'bullet_{n}.png'
        img = pg.image.load(f'{SS_PATH_IMG_BULLET}\{img_name}')
        return img

    def update(self):
        self.rect.centerx += 10
        self.animation()

    def animation(self):
        if self.freq_animation == SS_FREQ_ANIMATION:
            if self.pos_img < len(self.images):
                self.image = self.images[self.pos_img]
                self.pos_img += 1
            else:
                self.pos_img = 0
            self.freq_animation = 0
        else:
            self.freq_animation += 1

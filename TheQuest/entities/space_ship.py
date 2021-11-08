import pygame as pg
import os
from pygame import image

from pygame.sprite import Sprite
from TheQuest import IMAGES, RESOURCES, SC_HEIGHT, SC_WIDTH, SS_FREQ_ANIMATION, SS_LIFE_LIMIT, SS_IMG_SIZE, SS_PATH_SOUND_AST, SS_PATH_SOUND_BOX, SS_SPEED_Y
from util import SpriteSheet


class SpaceShip(Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = SpriteSheet(
            'rocket.jpg', 'rocket.json', (2, 20, 30))
        self.images = []
        #self.image = self.images[0]
        self.score = 0
        self.lives = SS_LIFE_LIMIT
        self.speed_y = SS_SPEED_Y
        self.sound_asteroid = pg.mixer.Sound(SS_PATH_SOUND_AST)
        self.repairing = False
        self.auto = False
        self.rep = 0
        self.initialize()
        self.freq_animation = SS_FREQ_ANIMATION
        self.pos_img = 0
        self.image = self.images[self.pos_img]
        self.rect = self.image.get_rect()

    def initialize(self):
        for x in range(1, 5):
            img = self.load_image('', x)
            img = pg.transform.scale(img, SS_IMG_SIZE)
            self.images.append(img)

    def load_image(self, mode, n):
        img_name = f'rocket_{mode}{n}.png'
        img = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'rocket', img_name))
        return img

    def update(self, *args, **kwargs):
        if self.auto:
            self.center_rocket()
            if self.rect.left < SC_WIDTH-50:
                self.rect.left += 1
            self.lading()
        else:
            self.move()

        self.animate()

    def move(self):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            self.rect.top -= self.speed_y
        elif pressed[pg.K_DOWN]:
            self.rect.bottom += self.speed_y

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SC_HEIGHT:
            self.rect.bottom = SC_HEIGHT

    def animate(self):
        if self.freq_animation == 0:
            if self.pos_img < len(self.images):
                self.image = self.images[self.pos_img]
                self.pos_img += 1
            else:
                self.pos_img = 0
            self.freq_animation = SS_FREQ_ANIMATION
        else:
            self.freq_animation -= 1

    def lading(self):
        pass

    def center_rocket(self):
        if self.rect.centery < SC_HEIGHT/2:
            self.rect.centery += 1
        elif self.rect.centery > SC_HEIGHT/2:
            self.rect.centery -= 1

    def collision_asteroids(self, asteroid_group):
        collisions = pg.sprite.spritecollide(self, asteroid_group, False)
        if self.repairing:
            pass
        elif len(collisions) > 0 and not self.repairing:
            for col in collisions:
                if not col.dodged:
                    self.lives -= 1
                    self.repairing = True
                    self.sound_asteroid.play()

    def collision_boxes(self, boxes_group):
        collisions = pg.sprite.spritecollide(self, boxes_group, True)
        if len(collisions) > 0:
            self.sound_box.play()

    def reset_rocket(self):
        if self.rep < 20:
            if self.pos_img < len(self.images):
                self.image = self.images[self.pos_img]
                self.pos_img += 1
            else:
                self.pos_img = 0

            self.rep += 1
        else:
            self.image = self.images[0]
            self.repairing = False
            self.rep = 0

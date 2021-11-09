import pygame as pg
import os
from pygame import image

from pygame.sprite import Sprite
from TheQuest import IMAGES, RESOURCES, SC_HEIGHT, SC_WIDTH, SS_FREQ_ANIMATION, SS_IMG_SIZE, SS_LOADING_TIME, SS_PATH_SOUND_AST, SS_SPEED_Y


class SpaceShip(Sprite):
    def __init__(self, time=0):
        super().__init__()
        self.pos_img = 0
        self.images = []
        self.load_images('loading')
        self.image = self.images[self.pos_img]
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, SC_HEIGHT/2)
        self.speed_y = SS_SPEED_Y
        self.sound_asteroid = pg.mixer.Sound(SS_PATH_SOUND_AST)
        self.auto = False
        self.loading = True
        self.collided = False
        self.time = time
        self.reload_time = self.time+SS_LOADING_TIME
        self.rep = 0
        self.freq_animation = SS_FREQ_ANIMATION
        self.angle = 0

    def load_images(self, mode=''):
        for x in range(1, 7):
            img = self.load_image(mode, x)
            #img = pg.transform.scale(img, SS_IMG_SIZE)
            self.images.append(img)

    def load_image(self, mode, n):
        img_name = f'rocket_{mode}{n}.png'
        img = pg.image.load(os.path.join(
            RESOURCES, IMAGES, 'rocket', img_name))
        return img

    def update(self, *args, **kwargs):
        if self.loading:
            ticks = pg.time.get_ticks()//1000
            if ticks > self.time:
                self.time = ticks
                print(self.time)
            if self.time == self.reload_time:
                self.images.clear()
                self.load_images()
                self.loading = False
            self.move()
        elif self.auto:
            self.center_rocket()
            if self.rect.left < SC_WIDTH-50:
                self.rect.left += 1
            else:
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
        self.angle += 10
        if self.angle <= 180:
            self.image = pg.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect()

    def center_rocket(self):
        if self.rect.centery < SC_HEIGHT/2:
            self.rect.centery += 1
        elif self.rect.centery > SC_HEIGHT/2:
            self.rect.centery -= 1

    def collision_asteroids(self, asteroid_group):
        if not self.loading and not self.auto:
            collisions = pg.sprite.spritecollide(self, asteroid_group, False)
            if len(collisions) > 0:
                self.sound_asteroid.play()
                self.collided = True

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

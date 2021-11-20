import pygame as pg
from pygame.sprite import Sprite
from TheQuest import FPS, SC_HEIGHT, SC_WIDTH, SS_BULLET_PER_SECOND, SS_FREQ_ANIMATION, SS_LOADING_TIME, SS_PATH_IMG_SHIP, SS_PATH_SOUND_AST, SS_SPEED_X, SS_SPEED_Y
from TheQuest.entities.bullet import Bullet


class SpaceShip(Sprite):
    def __init__(self, level):
        super().__init__()
        self.pos_img = 0
        self.images = []
        self.load_images('loading')
        self.image = self.images[self.pos_img]
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, SC_HEIGHT/2)
        self.speed_y = SS_SPEED_Y+level
        self.speed_x = SS_SPEED_X+level
        self.sound_asteroid = pg.mixer.Sound(SS_PATH_SOUND_AST)
        self.loading = True
        self.collided = False
        self.auto = False
        self.landed = False
        self.collide_animation = False
        self.time = 0
        self.freq_animation = SS_FREQ_ANIMATION
        self.frame = 0
        self.angle = 0
        self.bullets = pg.sprite.Group()
        self.frame_to_shoot = FPS/SS_BULLET_PER_SECOND
        self.frame_state = self.frame_to_shoot

    def load_images(self, mode=''):
        self.images.clear()
        for x in range(1, 7):
            img = self.load_image(mode, x)
            self.images.append(img)
        self.pos_img = 0
        print(f'Sequence of images loaded to: {mode}')

    def load_image(self, mode, n):
        img_name = f'rocket_{mode}{n}.png'
        img = pg.image.load(f'{SS_PATH_IMG_SHIP}\{img_name}')
        return img

    def update(self):
        if self.loading:
            self.count_frames()
            if self.time == SS_LOADING_TIME:
                self.load_images()
                self.loading = False
                print('Loading Ship completed')
            self.pressed_keys()
        elif self.auto:
            self.move_auto_y()
            self.move_auto_x()
        else:
            self.pressed_keys()
        self.animate()

    def count_frames(self):
        self.frame += 1
        if self.frame == FPS:
            self.time += 1
            self.frame = 0

    def move_auto_y(self):
        self.rect.centery = SC_HEIGHT/2

    def move_auto_x(self):
        if self.rect.left < SC_WIDTH-200:
            self.rect.centerx += 10
        else:
            self.landed = True
            self.rotating()

    def pressed_keys(self):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            self.rect.top -= self.speed_y

        if pressed[pg.K_DOWN]:
            self.rect.bottom += self.speed_y

        if pressed[pg.K_LEFT]:
            pass
            #self.rect.left -= self.speed_x

        if pressed[pg.K_RIGHT]:
            pass
            #self.rect.right += self.speed_x

        if pressed[pg.K_SPACE]:
            pass
            # self.shoot()
        self.verify_limits()

    def verify_limits(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SC_HEIGHT:
            self.rect.bottom = SC_HEIGHT

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH

    def rotating(self):
        if self.angle < 180:
            self.angle += 10
        else:
            self.angle = 180

    def animate(self):
        if self.freq_animation == SS_FREQ_ANIMATION:
            if self.pos_img < len(self.images):
                self.image = self.images[self.pos_img]
                self.pos_img += 1
            else:
                if self.collided:
                    self.collide_animation = False
                self.pos_img = 0
            self.freq_animation = 0
        else:
            self.freq_animation += 1

    def collision_asteroids(self, asteroid_group):

        if not self.loading and not self.auto:
            collisions = pg.sprite.spritecollide(self, asteroid_group, False)
            if len(collisions) > 0:
                print('Colisión!')
                self.sound_asteroid.play()
                self.load_images('explosion')
                self.collided = True
                self.collide_animation = True
                self.freq_animation = SS_FREQ_ANIMATION
                self.animate()

    def shoot(self):
        if self.frame_state == self.frame_to_shoot:
            self.bullets.add(Bullet(self.rect.midright))
            self.frame_state = 0
        else:
            self.frame_state += 1

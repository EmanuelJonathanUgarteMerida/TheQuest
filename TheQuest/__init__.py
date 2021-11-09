import os

import pygame

# DIR
RESOURCES = 'resources'
SOUNDS = 'sounds'
FONTS = 'fonts'
IMAGES = 'images'

# Screen
SC_HEIGHT = 720
SC_WIDTH = 1280

# Player
SS_IMG_SIZE = (123, 67)
SS_SPEED_Y = 2
SS_LIFE_LIMIT = 5
SS_BONUS_LEVEL = 200
SS_FREQ_ANIMATION = 2
SS_PATH_IMG_SHIP = os.path.join(RESOURCES, IMAGES, 'rocket.jpg')
SS_PATH_SOUND_BOX = os.path.join(RESOURCES, SOUNDS, 'collision_box.mp3')
SS_PATH_SOUND_AST = os.path.join(RESOURCES, SOUNDS, 'collision_asteroid.mp3')
SS_TIME_REPAIRING = 3
SS_LOADING_TIME = 2

# Asteroid
AS_SPEED_X = 5
AS_PATH_IMG = os.path.join(RESOURCES, IMAGES, 'asteroids_sheet.png')
AS_PATH_JSON = os.path.join(RESOURCES, IMAGES, 'asteroids_sheet.json')

# Box_Object
BO_OBJECTS = [('live_up', ('HP_Bonus.png', 1)), ('speed_up', ('Enemy_Speed_Debuff.png', 2)),
              ('barrier', ('Barrier_Bonus.png', 1200)), ('fuel', ('Rockets_Bonus.png', 100)), ('space_trash', ('Hero_Speed_Debuff.png', -100, -2))]

# Game
FPS = 60
G_PATH_IMG = os.path.join(RESOURCES, IMAGES, 'background', 'space_1.png')
G_LEVEL_LIMIT_TIME = 10
G_LIVES_LIMIT = 3

# ScoreBoard
SB_TITLE_FONT = 'GameCube.ttf'
SB_BOARD_FONT = 'GameCube.ttf'
SB_PATH_FONT_BOARD = os.path.join(RESOURCES, FONTS, SB_BOARD_FONT)
SB_SIZE_BOARD_TEXT = 30
SB_COLOR_BOARD_TEXT = (255, 255, 255)
SB_POS_SCORE_PLAYER = (10, 10)
SB_POS_LIVES_PLAYER = (100, 10)
SB_POS_LEVEL_GAME = (SC_WIDTH/2, 10)
SB_POS_TIME_GAME = (SC_WIDTH-10, 10)

import os

import pygame

# DIR
RESOURCES = 'resources'
SOUNDS = 'sounds'
FONTS = 'fonts'
IMAGES = 'images'
BG = 'background'

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
AS_LIMITS_X = (0, SC_WIDTH)
AS_LIMITS_Y = (0, SC_HEIGHT)
AS_SPEED_X_FINISH = 10

# Game
FPS = 60
G_PATH_IMG = os.path.join(RESOURCES, IMAGES, BG, 'space_1.png')
G_LEVEL_LIMIT_TIME = 5
G_LIVES_LIMIT = 3

# ScoreBoard
SB_TITLE_FONT = 'Games.ttf'
SB_BOARD_FONT = 'Games.ttf'
SB_PATH_FONT_BOARD = os.path.join(RESOURCES, FONTS, SB_BOARD_FONT)
SB_SIZE_BOARD_TEXT = 20
SB_COLOR_BOARD_TEXT = (255, 255, 255)
SB_POS_SCORE_PLAYER = (10, 10)
SB_MARGIN_TOP = 10
SB_POS_LIVES_PLAYER = ((SC_WIDTH/4), SB_MARGIN_TOP)
SB_POS_LEVEL_GAME = (SC_WIDTH/2, SB_MARGIN_TOP)
SB_POS_TIME_GAME = (SC_WIDTH-10, SB_MARGIN_TOP)

# Presentation
PR_PATH_BG = os.path.join(RESOURCES, IMAGES, BG, 'bg.jpg')
PR_DESC = 'El planeta tierra colapsó en el año 2050, \ny los pocos sobrevivientes lograron escapar en la nave \"Quest\"\n en busca de un nuevo planeta el cual habitar'

# DBManager
DBM_PATH = 'data/thequest.db'

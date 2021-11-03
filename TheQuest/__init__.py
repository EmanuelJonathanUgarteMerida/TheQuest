import os

# DIR
RESOURCES = 'resources'
SOUNDS = 'sounds'
IMAGES = 'images'

# Screen
SC_HEIGHT = 500
SC_WIDTH = 1080

# Player
SS_IMG_SIZE = (50, 50)
SS_SPEED_Y = 2
SS_LIFE_LIMIT = 5
SS_BONUS_LEVEL = 200
SS_PATH_IMG_SHIP = os.path.join(RESOURCES, IMAGES, 'space_ship.png')
SS_PATH_SOUND_BOX = os.path.join(RESOURCES, SOUNDS, 'collision_box.mp3')
SS_PATH_SOUND_AST = os.path.join(RESOURCES, SOUNDS, 'collision_asteroid.mp3')

# Asteroid
AS_SPEED_X = 5

# Box_Object
BO_OBJECTS = [('live_up', ('HP_Bonus.png', 1)), ('speed_up', ('Enemy_Speed_Debuff.png', 2)),
              ('barrier', ('Barrier_Bonus.png', 1200)), ('fuel', ('Rockets_Bonus.png', 100)), ('space_trash', ('Hero_Speed_Debuff.png', -100, -2))]

# Game
FPS = 60

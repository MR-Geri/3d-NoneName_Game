import numpy as np


# game settings
WIDTH, HEIGHT = 1800, 1000
FPS = 60
BLOCK_TITLE = 100
FPS_POS = (WIDTH - 50, 5)


# player settings
player_pos = (WIDTH // 2, HEIGHT // 2)
player_angle = 0
player_speed = 2
player_angle_speed = 0.03

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 180, 255)
RED = (255, 0, 0)
GREEN = (0, 80, 0)
YELLOW = (220, 220, 0)

# ray casting settings
FOV = np.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = WIDTH
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))
COEFFICIENT = DIST * BLOCK_TITLE
SCALE = WIDTH // NUM_RAYS

# mini-maps
MAP_SCALE = 5
MAP_TITLE = BLOCK_TITLE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

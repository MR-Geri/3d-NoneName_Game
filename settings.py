import pygame
import numpy as np


# game settings
WIDTH, HEIGHT = 1800, 1000
FPS = 60
BLOCK_TITLE = 100
sc = pygame.display.set_mode((WIDTH, HEIGHT))


# player settings
player_pos = (WIDTH // 2, HEIGHT // 2)
player_angle = 0
player_speed = 10
player_angle_speed = 0.03

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (207, 74, 100)

# ray casting settings
FOV = np.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = WIDTH
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))
COEFFICIENT = 3 * DIST * BLOCK_TITLE
SCALE = WIDTH // NUM_RAYS

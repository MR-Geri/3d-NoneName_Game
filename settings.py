import pygame


# game settings
WIDTH, HEIGHT = 1900, 1000
FPS = 60
BLOCK_TITLE = 100
sc = pygame.display.set_mode((WIDTH, HEIGHT))


# player settings
player_pos = (WIDTH // 2, HEIGHT // 2)
player_angle = 0
player_speed = 5
player_angle_speed = 0.03

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

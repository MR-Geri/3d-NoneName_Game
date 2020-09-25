from settings import *
from player import Player
from map import Map
from ray_casting import ray_casting

import pygame
import numpy as np

pygame.init()
clock = pygame.time.Clock()
player = Player()
map_ = Map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.move()
    sc.fill(BLACK)
    #
    # pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HEIGHT // 2))
    # pygame.draw.rect(sc, GRAY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    ray_casting(map_, player.pos, player.angle)
    # map_.draw()
    # pygame.draw.circle(sc, WHITE, player.pos, 10)
    # pygame.draw.line(sc, WHITE, player.pos, (
    #     player.x + WIDTH * np.cos(player.angle),
    #     player.y + WIDTH * np.sin(player.angle)
    # ))
    #
    pygame.display.update()
    clock.tick(FPS)

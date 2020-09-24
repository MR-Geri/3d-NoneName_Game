from settings import *
from player import Player
from map import Map

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
    map_.draw()
    pygame.draw.circle(sc, WHITE, player.pos, 10)
    pygame.draw.line(sc, WHITE, player.pos, (
        player.x + WIDTH * np.cos(player.angle),
        player.y + WIDTH * np.sin(player.angle)
    ))
    #
    pygame.display.update()
    clock.tick(FPS)

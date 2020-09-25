from settings import *
from player import Player
from drawing import Drawing

import pygame

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.move()
    sc.fill(BLACK)
    #
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    #
    pygame.display.update()
    clock.tick(FPS)

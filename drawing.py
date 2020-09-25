from settings import *
from ray_casting import ray_casting
from map import mini_map

import pygame
import numpy as np


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc, self.sc_map = sc, sc_map
        self.font = pygame.font.SysFont('TimesNewRoman', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.sc, GRAY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    def world(self, pos, angle):
        ray_casting(self.sc, pos, angle)

    def fps(self, clock):
        render = self.font.render(f'{int(clock.get_fps())}', 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        x, y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(
            self.sc_map, YELLOW,
            (x, y),
            (x + 12 * np.cos(player.angle), y + 12 * np.sin(player.angle)),
            2
        )
        pygame.draw.circle(self.sc_map, GREEN, (x, y), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TITLE, MAP_TITLE))
        self.sc.blit(self.sc_map, MAP_POS)

from settings import *
import pygame


map_ = [
    '###################',
    '#                 #',
    '#                 #',
    '#                 #',
    '#                 #',
    '#                 #',
    '#                 #',
    '#                 #',
    '#                 #',
    '###################'
]


class Map:
    def __init__(self):
        self.world_map = set()
        for y, row in enumerate(map_):
            for x, char in enumerate(row):
                if char == '#':
                    self.world_map.add((x * BLOCK_TITLE, y * BLOCK_TITLE))

    def draw(self):
        for x, y in self.world_map:
            pygame.draw.rect(sc, GRAY, (x, y, BLOCK_TITLE, BLOCK_TITLE), 5)

from settings import *
import pygame


maps = [
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

world_map = set()
for y, row in enumerate(maps):
    for x, char in enumerate(row):
        if char == '#':
            world_map.add((x * BLOCK_TITLE, y * BLOCK_TITLE))

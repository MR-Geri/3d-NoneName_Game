from settings import *


maps = [
    '##################',
    '#                #',
    '#                #',
    '#                #',
    '#                #',
    '#                #',
    '#                #',
    '#                #',
    '#                #',
    '##################'
]

world_map = set()
mini_map = set()
for y, row in enumerate(maps):
    for x, char in enumerate(row):
        if char == '#':
            world_map.add((x * BLOCK_TITLE, y * BLOCK_TITLE))
            mini_map.add((x * MAP_TITLE, y * MAP_TITLE))

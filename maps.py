import pygame

WALL = 1
EMPTY = 0

W = WALL
X = EMPTY

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

sub1 = [
    [W, W, W, W, W, W, W, W, W, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, X, X, X, X, X, X, X, X, W],
    [W, W, W, W, W, W, W, W, W, W]
]

def draw_map(current_map, tile_width, tile_height):
    tile_render_stack = []
    for col in range(10):
        for row in range(10):
            tile = pygame.Rect((col*tile_width, row*tile_height, tile_width, tile_height))

            tile_color = WHITE
            if current_map[row][col] == EMPTY:
                tile_color = WHITE
            elif current_map[row][col] == WALL:
                tile_color = BLACK

            tile_render_stack.append((tile, False, tile_color))
    return tile_render_stack

import pygame
from namespace import *
import gamestate as game
import math

# H - Hull
# X - Empty/Floor

sub1 = [
    [H, H, H, H, H, H, H, H, H, H, X, H, H, H, H, H, H, H, H, H],
    [H, F, F, F, F, F, F, F, F, H, X, H, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, H, X, H, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, H, H, H, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, F, D, F, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, F, D, F, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, H, H, H, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, H, X, H, F, F, F, F, F, F, F, H],
    [H, F, F, F, F, F, F, F, F, H, X, H, F, F, F, F, F, F, F, H],
    [H, H, H, H, H, H, H, H, H, H, X, H, H, H, H, H, H, H, H, H]
]

def draw_map():
    tile_surface = pygame.Surface((game.TILE_WIDTH*len(game.CURRENT_MAP[0]), game.TILE_HEIGHT*len(game.CURRENT_MAP)))
    for col in range(len(game.CURRENT_MAP[0])):
        for row in range(len(game.CURRENT_MAP)):
            #tile = pygame.Rect((col*TILE_WIDTH-camera_position[0], row*TILE_HEIGHT-camera_position[1], TILE_WIDTH, TILE_HEIGHT))
            if(game.CURRENT_MAP[row][col] == WATER):
                continue
            if game.MAIN_CAMERA.in_range((game.TILE_WIDTH*col, game.TILE_HEIGHT*row)):
                tile_img = pygame.image.load(TILE_TO_IMAGE_REF[game.CURRENT_MAP[row][col]])

                tile_img = pygame.transform.scale(tile_img, (game.TILE_WIDTH, game.TILE_HEIGHT))
                tile_surface.blit(tile_img, (game.TILE_WIDTH*col, game.TILE_HEIGHT*row))
            else:
                continue

    return (tile_surface, (0,0))

def area_to_tile(position, size):
    left_x = math.floor(position[0]/game.TILE_WIDTH)
    right_x = math.floor((position[0]+size[0])/game.TILE_WIDTH)

    top_y = math.floor(position[1]/game.TILE_HEIGHT)
    bottom_y = math.floor((position[1]+size[1])/game.TILE_HEIGHT)

    middle_x = math.floor((position[0]+(size[0]/2))/game.TILE_HEIGHT)
    middle_y = math.floor((position[1]+(size[1]/2))/game.TILE_HEIGHT)

    tiles_touched = set()
    try:
        top_left_tile = game.CURRENT_MAP[top_y][left_x]
        tiles_touched.add(top_left_tile)
    except:
        ...
    try:
        top_right_tile = game.CURRENT_MAP[top_y][right_x]
        tiles_touched.add(top_right_tile)
    except:
        ...
    try:
        bottom_left_tile = game.CURRENT_MAP[bottom_y][left_x]
        tiles_touched.add(bottom_left_tile)
    except:
        ...
    try:
        bottom_right_tile = game.CURRENT_MAP[bottom_y][right_x]
        tiles_touched.add(bottom_right_tile)
    except:
        ...
    try:
        middle_tile = game.CURRENT_MAP[middle_y][middle_x]
    except:
        middle_tile = None
    tiles_touched = list(tiles_touched)

    return middle_tile, tiles_touched

def area_touching_tile(position, size, tile):
    # If the position given is outside of the map, simply return False
    discard, tiles_touched = area_to_tile(position, size)
    if isinstance(tile, list):
        for t in tile:
            if t in tiles_touched:
                return True
        return False
    else:
        return tile in tiles_touched


import pygame
from namespace import *
import gamestate as game
import math

# H - Hull
# X - Empty/Floor

sub1 = [
    [H, H, H, H, H, H, H, H, H, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, H],
    [H, X, X, X, X, X, X, X, X, D, X],
    [H, X, X, X, X, X, X, X, X, D, X],
    [H, X, X, X, X, X, X, X, X, H, H],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, H, H, H, H, H, H, H, H, H, X]
]

def draw_map():
    tile_surface = pygame.Surface((game.TILE_WIDTH*len(game.CURRENT_MAP[0]), game.TILE_HEIGHT*len(game.CURRENT_MAP)))
    for col in range(len(game.CURRENT_MAP[0])):
        for row in range(len(game.CURRENT_MAP)):
            #tile = pygame.Rect((col*TILE_WIDTH-camera_position[0], row*TILE_HEIGHT-camera_position[1], TILE_WIDTH, TILE_HEIGHT))
            if game.MAIN_CAMERA.in_range((game.TILE_WIDTH*col, game.TILE_HEIGHT*row)):
                if game.CURRENT_MAP[row][col] == EMPTY:
                    tile_img = pygame.image.load(FLOOR_TILE)
                elif game.CURRENT_MAP[row][col] == HULL:
                    tile_img = pygame.image.load(HULL_TILE)
                elif game.CURRENT_MAP[row][col] == DOOR:
                    tile_img = pygame.image.load(DOOR_TILE)
                else:
                    tile_img = pygame.image.load(PLACEHOLDER)
                
                tile_img = pygame.transform.scale(tile_img, (game.TILE_WIDTH, game.TILE_HEIGHT))
                tile_surface.blit(tile_img, (game.TILE_WIDTH*col, game.TILE_HEIGHT*row))
            else:
                continue

    return (tile_surface, (0,0))

def position_to_tile(position):
    left_x = math.floor(position[0]/game.TILE_WIDTH)
    right_x = math.floor((position[0]+game.PLAYER_SIZE)/game.TILE_WIDTH)

    top_y = math.floor(position[1]/game.TILE_HEIGHT)
    bottom_y = math.floor((position[1]+game.PLAYER_SIZE)/game.TILE_HEIGHT)

    middle_x = math.floor((position[0]+(game.PLAYER_SIZE/2))/game.TILE_HEIGHT)
    middle_y = math.floor((position[1]+(game.PLAYER_SIZE/2))/game.TILE_HEIGHT)

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

def touching_tile(position, tile):
    # If the position given is outside of the map, simply return False
    discard, tiles_touched = position_to_tile(position)
    if isinstance(tile, list):
        for t in tile:
            if t in tiles_touched:
                return True
        return False
    else:
        return tile in tiles_touched


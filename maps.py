import pygame
from namespace import *
from gamestate import *

# H - Hull
# X - Empty/Floor

sub1 = [
    [H, H, H, H, H, H, H, H, H, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, H],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, H],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, X, X, X, X, X, X, X, X, H, X],
    [H, H, H, H, H, H, H, H, H, H, X]
]

def draw_map():
    tile_surface = pygame.Surface((TILE_WIDTH*len(CURRENT_MAP[0]), TILE_HEIGHT*len(CURRENT_MAP)))
    for col in range(len(CURRENT_MAP[0])):
        for row in range(len(CURRENT_MAP)):
            #tile = pygame.Rect((col*TILE_WIDTH-camera_position[0], row*TILE_HEIGHT-camera_position[1], TILE_WIDTH, TILE_HEIGHT))
            if MAIN_CAMERA.in_range((TILE_WIDTH*col, TILE_HEIGHT*row)):
                if CURRENT_MAP[row][col] == EMPTY:
                    tile_img = pygame.image.load(FLOOR_TILE)
                elif CURRENT_MAP[row][col] == HULL:
                    tile_img = pygame.image.load(HULL_TILE)
                else:
                    tile_img = pygame.image.load(PLACEHOLDER)
                
                tile_img = pygame.transform.scale(tile_img, (TILE_WIDTH, TILE_HEIGHT))
                tile_surface.blit(tile_img, (TILE_WIDTH*col, TILE_HEIGHT*row))
            else:
                continue

    return (tile_surface, (0,0))

def position_to_tile(position):
    position[0]/TILE_WIDTH

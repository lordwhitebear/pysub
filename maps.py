import pygame
import namespace

HULL = 1
EMPTY = 0

H = HULL
X = EMPTY

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

def draw_map(current_map, tile_width, tile_height, camera_position):
    tile_surface = pygame.Surface((tile_width*len(current_map[0]), tile_height*len(current_map)))
    for col in range(len(current_map[0])):
        for row in range(len(current_map)):
            #tile = pygame.Rect((col*tile_width-camera_position[0], row*tile_height-camera_position[1], tile_width, tile_height))

            if current_map[row][col] == EMPTY:
                tile_img = pygame.image.load(namespace.FLOOR_TILE)
            elif current_map[row][col] == HULL:
                tile_img = pygame.image.load(namespace.HULL_TILE)
            else:
                tile_img = pygame.image.load(namespace.PLACEHOLDER)
            
            tile_img = pygame.transform.scale(tile_img, (tile_width, tile_height))
            tile_surface.blit(tile_img, (tile_width*col, tile_height*row))

    return (tile_surface, (0,0))

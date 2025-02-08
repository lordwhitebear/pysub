import pygame

# Image assets
PLACEHOLDER = "assets/placeholder.png"
DOOR_CLOSED_TILE = "assets/door_closed_tile.png"
DOOR_OPEN_TILE = "assets/door_open_tile.png"
HULL_TILE = "assets/hull_tile.png"
FLOOR_TILE = "assets/floor_tile.png"

# Keybinds
KEY_UP = pygame.K_UP
KEY_UP_ALT = 119 # "w"
KEY_DOWN = pygame.K_DOWN
KEY_DOWN_ALT = 115 # "s"
KEY_RIGHT = pygame.K_RIGHT
KEY_RIGHT_ALT = 100 # "d"
KEY_LEFT = pygame.K_LEFT
KEY_LEFT_ALT = 97 # "a"
KEY_INTERACT = 101 # "e"

# Map namespace
DOOR_CLOSED = 3
DOOR_OPEN = 2
HULL = 1
FLOOR = 0
WATER = -1
D = DOOR_CLOSED
d = DOOR_OPEN
H = HULL
F = FLOOR
X = WATER
SOLID_TILES = [HULL, DOOR_CLOSED] # Contains all tiles that cannot be walked through

# Tile-to-image
TILE_TO_IMAGE_REF = {
    DOOR_CLOSED: DOOR_CLOSED_TILE,
    DOOR_OPEN: DOOR_OPEN_TILE,
    HULL: HULL_TILE,
    FLOOR: FLOOR_TILE
}

# Camera modes
FREE_CAM = 1
FOLLOW = 2

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
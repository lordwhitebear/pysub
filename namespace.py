import pygame

# Image assets
PLACEHOLDER = "assets/placeholder.png"
DOOR_TILE = "assets/door_tile.png"
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

# Map namespace
DOOR = 2
HULL = 1
EMPTY = 0
D = DOOR
H = HULL
X = EMPTY
SOLID_TILES = [HULL] # Contains all tiles that cannot be walked through

# Camera modes
FREE_CAM = 1
FOLLOW = 2

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
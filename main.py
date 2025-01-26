import pygame
import maps
import player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TILE_GRID = 10
TILE_WIDTH = SCREEN_WIDTH/TILE_GRID
TILE_HEIGHT = SCREEN_HEIGHT/TILE_GRID

CURRENT_MAP = maps.sub1

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


rect_render_stack = []

def start():
    # Create main game canvas
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create main player
    global player1
    player1 = player.Player((100, 100, 50, 50))

def handle_keystroke(key):
    pass


def update():
    # Add map tiles to the render stack
    for tile in maps.draw_map(CURRENT_MAP, TILE_WIDTH, TILE_HEIGHT):
        rect_render_stack.append(tile)

    # Create player1 rect
    player1_rect = pygame.Rect(player1.get_transform())
    rect_render_stack.append((player_rect, False, RED))

    key = pygame.key.get_pressed


def render():
    global rect_render_stack
    rects_drawn = 0
    for rect in rect_render_stack:
        # If rect is an image
        if rect[1]:
            pass
        else:
            # rect[2] is rect color, rect[0] is the rect object
            pygame.draw.rect(screen, rect[2], rect[0])
            rects_drawn += 1
    rect_render_stack = []
    print(rects_drawn)
    rects_drawn = 0
    pygame.display.update()

def main():
    #INIT
    pygame.init()
    start()
    #MAIN LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        update()
        render()

if __name__ == "__main__":
    main()
    pygame.quit()

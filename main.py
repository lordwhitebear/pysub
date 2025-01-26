import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TILE_GRID = 10
TILE_WIDTH = SCREEN_WIDTH/TILE_GRID
TILE_HEIGHT = SCREEN_HEIGHT/TILE_GRID

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect_render_stack = []

def update():
    player = pygame.Rect((100, 100, 50, 50))
    rect_render_stack.append((player, False, WHITE))

    for col in range(10):
        for row in range(10):
            tile = pygame.Rect((col*TILE_WIDTH, row*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            rect_render_stack.append((tile, False, BLUE))

    return rect_render_stack

def render(rect_render_stack):
    for rect in rect_render_stack:
        # If rect is an image
        if rect[1]:
            pass
        else:
            # rect[2] is rect color, rect[0] is the rect object
            pygame.draw.rect(screen, rect[2], rect[0])

    pygame.display.update()

def main():
    #INIT
    pygame.init()
    # Create main game canvas
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #MAIN LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rect_render_stack = update()
        render(rect_render_stack)

if __name__ == "__main__":
    main()
    pygame.quit()

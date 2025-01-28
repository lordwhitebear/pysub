import pygame
import maps
import player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

FPS = 60.0

TILE_GRID = 10
TILE_WIDTH = SCREEN_WIDTH/TILE_GRID
TILE_HEIGHT = SCREEN_HEIGHT/TILE_GRID

KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT

CURRENT_MAP = maps.sub1

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PLAYER_SIZE = 50
PLAYER_SPEED = 100

rect_render_stack = []

def start():
    # Create main game canvas
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    global clock
    clock=pygame.time.Clock()
    # Create main player
    global player1
    player1 = player.Player((100, 100, PLAYER_SIZE, PLAYER_SIZE))
    # Create camera

def handle_keystroke(keys):
    # Up key pressed
    if keys[KEY_UP] and not keys[KEY_DOWN]:
        player_transform = player1.get_transform()
        new_player_transform = (player_transform[0], player_transform[1]-(PLAYER_SPEED*dt), player_transform[2], player_transform[3])
        player1.set_transform(new_player_transform)
    # Down key pressed
    if keys[KEY_DOWN] and not keys[KEY_UP]:
        player_transform = player1.get_transform()
        new_player_transform = (player_transform[0], player_transform[1]+(PLAYER_SPEED*dt), player_transform[2], player_transform[3])
        player1.set_transform(new_player_transform)
    # Right key pressed
    if keys[KEY_RIGHT] and not keys[KEY_LEFT]:
        player_transform = player1.get_transform()
        new_player_transform = (player_transform[0]+(PLAYER_SPEED*dt), player_transform[1], player_transform[2], player_transform[3])
        player1.set_transform(new_player_transform)
    # Left key pressed
    if keys[KEY_LEFT] and not keys[KEY_RIGHT]:
        player_transform = player1.get_transform()
        new_player_transform = (player_transform[0]-(PLAYER_SPEED*dt), player_transform[1], player_transform[2], player_transform[3])
        player1.set_transform(new_player_transform)

def update():
    # Calculate DeltaTime
    global dt
    dt = clock.tick() / 1000
    try:
        print(1/dt)
    except:
        ...
    # Add map tiles to the render stack
    for tile in maps.draw_map(CURRENT_MAP, TILE_WIDTH, TILE_HEIGHT):
        rect_render_stack.append(tile)

    # Create player1 rect
    player1_rect = pygame.Rect(player1.get_transform())
    rect_render_stack.append((player1_rect, False, RED))

    # Handle keystrokes
    key = pygame.key.get_pressed()
    handle_keystroke(key)

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

import pygame
import maps
import player
import camera

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

MAIN_CAMERA = None

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PLAYER_SIZE = 50
PLAYER_SPEED = 200

rect_render_stack = []

def start():
    # Create main game canvas
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create clock to train game tick
    global clock
    clock=pygame.time.Clock()
    # Create main player
    global player1
    player1 = player.Player((380, 380), PLAYER_SIZE)
    # Create camera
    global MAIN_CAMERA
    camera1 = camera.Camera((400, 400), ((-SCREEN_WIDTH/2)+PLAYER_SIZE/2, (-SCREEN_HEIGHT/2)+PLAYER_SIZE/2), player1)
    MAIN_CAMERA = camera1
    

def handle_keystroke(keys):
    # Up key pressed
    if keys[KEY_UP] and not keys[KEY_DOWN]:
        player_position = player1.get_position()
        new_player_position = (player1.get_position()[0], player1.get_position()[1]-(PLAYER_SPEED*dt))
        player1.set_position(new_player_position)
    # Down key pressed
    if keys[KEY_DOWN] and not keys[KEY_UP]:
        player_position = player1.get_position()
        new_player_position = (player1.get_position()[0], player1.get_position()[1]+(PLAYER_SPEED*dt))
        player1.set_position(new_player_position)
    # Right key pressed
    if keys[KEY_RIGHT] and not keys[KEY_LEFT]:
        player_position = player1.get_position()
        new_player_position = (player1.get_position()[0]+(PLAYER_SPEED*dt), player1.get_position()[1])
        player1.set_position(new_player_position)
    # Left key pressed
    if keys[KEY_LEFT] and not keys[KEY_RIGHT]:
        player_position = player1.get_position()
        new_player_position = (player1.get_position()[0]-(PLAYER_SPEED*dt), player1.get_position()[1])
        player1.set_position(new_player_position)

def update():
    # Calculate DeltaTime
    global dt
    dt = clock.tick() / 1000
    try:
        print(1/dt)
    except:
        ...

    # Update camera position
    MAIN_CAMERA.update()

    # Add map tiles to the render stack
    for tile in maps.draw_map(CURRENT_MAP, TILE_WIDTH, TILE_HEIGHT, MAIN_CAMERA.get_position()):
        rect_render_stack.append(tile)

    # Create player1 rect
    player1_rect = pygame.Rect((player1.get_position()[0]-MAIN_CAMERA.get_position()[0], player1.get_position()[1]-MAIN_CAMERA.get_position()[1], PLAYER_SIZE, PLAYER_SIZE))
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

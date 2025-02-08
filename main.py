import pygame
import maps
import player
import camera
from namespace import *
import gamestate as game

rect_render_stack = []
surface_render_stack = []

def start():
    # Create main game canvas
    global screen
    screen = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
    # Create clock to train game tick
    global clock
    clock=pygame.time.Clock()
    # Frames since start
    global progressed_frames
    progressed_frames = 0
    # Create main player
    global player1
    player1 = player.Player((380, 380), game.PLAYER_SIZE)
    # Create camera
    camera1 = camera.Camera((400, 400), ((-game.SCREEN_WIDTH/2)+game.PLAYER_SIZE/2, (-game.SCREEN_HEIGHT/2)+game.PLAYER_SIZE/2), player1)
    game.MAIN_CAMERA = camera1
    # Set current map
    game.CURRENT_MAP = maps.sub1
    

def handle_keystroke(keys):
    # Up key pressed
    if (keys[KEY_UP] or keys[KEY_UP_ALT]) and not (keys[KEY_DOWN] or keys[KEY_DOWN_ALT]):
        new_position = (player1.get_position()[0], player1.get_position()[1]-(game.PLAYER_SPEED*dt))
        if not maps.touching_tile(new_position, SOLID_TILES):
            player1.set_position(new_position)
    # Down key pressed
    if (keys[KEY_DOWN] or keys[KEY_DOWN_ALT]) and not (keys[KEY_UP] or keys[KEY_UP_ALT]):
        new_position = (player1.get_position()[0], player1.get_position()[1]+(game.PLAYER_SPEED*dt))
        if not maps.touching_tile(new_position, SOLID_TILES):
            player1.set_position(new_position)
    # Right key pressed
    if (keys[KEY_RIGHT] or keys[KEY_RIGHT_ALT]) and not (keys[KEY_LEFT] or keys[KEY_LEFT_ALT]):
        new_position = (player1.get_position()[0]+(game.PLAYER_SPEED*dt), player1.get_position()[1])
        if not maps.touching_tile(new_position, SOLID_TILES):
            player1.set_position(new_position)
    # Left key pressed
    if (keys[KEY_LEFT] or keys[KEY_LEFT_ALT]) and not (keys[KEY_RIGHT] or keys[KEY_RIGHT_ALT]):
        new_position = (player1.get_position()[0]-(game.PLAYER_SPEED*dt), player1.get_position()[1])
        if not maps.touching_tile(new_position, SOLID_TILES):
            player1.set_position(new_position)


def update():
    # Calculate DeltaTime
    global dt, progressed_frames
    dt = clock.tick() / 1000
    try:
        if(progressed_frames % 200 == 0):
            print("fps:", 1/dt)
    except:
        ...

    # Update camera position
    game.MAIN_CAMERA.update()

    # Draw Map
    tile_surface, tile_surface_position = maps.draw_map()
    # Modify tile_surface_position by camera position
    tile_surface_position = (tile_surface_position[0]-game.MAIN_CAMERA.get_position()[0], tile_surface_position[1]-game.MAIN_CAMERA.get_position()[1])
    # Adds drawn map tile surface to the surface render stack
    surface_render_stack.append((tile_surface, tile_surface_position))

    # Create player1 rect
    player1_rect = pygame.Rect((player1.get_position()[0]-game.MAIN_CAMERA.get_position()[0], player1.get_position()[1]-game.MAIN_CAMERA.get_position()[1], game.PLAYER_SIZE, game.PLAYER_SIZE))
    rect_render_stack.append((player1_rect, RED))

    # Handle keystrokes
    key = pygame.key.get_pressed()
    handle_keystroke(key)

    # Increase progressed frames tracker
    progressed_frames += 1

def render():
    global rect_render_stack, surface_render_stack
    # Track number of drawn objects
    surfaces_drawn = 0
    rects_drawn = 0

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw surfaces
    for surface in surface_render_stack:
        # surface[0] is the surface object, surface[1] is a tuple representing the surfaces position
        screen.blit(surface[0], surface[1])
        surfaces_drawn += 1
    surface_render_stack = []

    # Draw rectangles
    for rect in rect_render_stack:
        # rect[1] is color, rect[0] is the rect object
        pygame.draw.rect(screen, rect[1], rect[0])
        rects_drawn += 1
    rect_render_stack = []

    rects_drawn, surfaces_drawn = 0, 0

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

import math
import gamestate as game

def is_point_colliding(point, object_pos, object_size):
    if(point[0] > object_pos[0] and point[0] < object_pos[0]+object_size[0]): # Within horizontal constraint
        if(point[1] > object_pos[1] and point[1] < object_pos[1]+object_size[1]): # Within vertical constraint
            return True
    return False

def is_colliding(object1_pos, object1_size, object2_pos, object2_size):
    # Check if each corner of object1 is colling with object2
    if is_point_colliding(object1_pos, object2_pos, object2_size):
        return True
    if is_point_colliding((object1_pos[0]+object1_size[0], object1_pos[1]), object2_pos, object2_size):
        return True
    if is_point_colliding((object1_pos[0], object1_pos[1]+object1_size[1]), object2_pos, object2_size):
        return True
    if is_point_colliding((object1_pos[0]+object1_size[0], object1_pos[1]+object1_size[1]), object2_pos, object2_size):
        return True
    return False

def tile_to_coordinate(tile):
    return (tile[1] * game.TILE_WIDTH, tile[0] * game.TILE_HEIGHT)

def coordinate_to_tile(coordinate):
    return (math.floor(coordinate[0]/game.TILE_WIDTH), math.floor(coordinate[1]/game.TILE_HEIGHT))
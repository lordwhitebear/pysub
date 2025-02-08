import helpers
import gamestate as game
from namespace import *

class DoorController:
    __slots__ = ["__position", "__scale", "__doors"]
    def __init__(self, position, scale, doors):
        self.__position = position
        self.__scale = scale
        self.__doors = doors

    def trigger(self):
        # Check if doors are open or closed
        door = self.__doors[0]
        # If the doors are open
        if game.CURRENT_MAP[door[0]][door[1]] == DOOR_OPEN:
            for door in self.__doors:
                game.CURRENT_MAP[door[0]][door[1]] = DOOR_CLOSED
        else:
            for door in self.__doors:
                game.CURRENT_MAP[door[0]][door[1]] = DOOR_OPEN

    def in_range(self, player):
        return helpers.is_colliding(player.get_position(), (game.PLAYER_SIZE, game.PLAYER_SIZE), self.__position, self.__scale)
    
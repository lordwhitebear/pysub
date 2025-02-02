import pygame
from enum import Enum

class CameraModes(Enum):
    FREE_CAM = 1
    FOLLOW = 2

class Camera:
    __slots__ = ["__position", "__offset", "__focus", "__mode"]
    def __init__(self, position, offset, focus, mode=CameraModes.FREE_CAM):
        self.__position = position
        self.__focus = focus
        self.__mode = mode
        self.__offset = offset

    def get_position(self):
        return self.__position
    
    def get_focus(self):
        return self.__focus
    
    def get_mode(self):
        return self.__mode
    
    def set_position(self, position):
        if self.__mode == CameraModes.FREE_CAM:
            self.__position = position
        else:
            raise("Camera must be in Free-Cam to set position.")
        
    def set_offset(self, offset):
        self.__offset = offset
        
    def set_focus(self, focus):
        self.__focus = focus
        
    def update(self):
        if self.__mode == CameraModes.FREE_CAM:
            try:
                self.__position = (self.__focus.get_position()[0] + self.__offset[0], self.__focus.get_position()[1] + self.__offset[1])
            except:
                print(self + " could not get focus position.")
        
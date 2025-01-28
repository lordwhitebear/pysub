import pygame

class Player:
    __slots__ = ["__position", "__scale", "__image", "__color"]
    def __init__(self, position, scale, image=None, color=(255, 255, 255)):
        self.__position = position
        self.__scale = scale
        self.__image = image
        self.__color = color

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position
    
    def get_image(self):
        return self.__image
    
    def get_color(self):
        return self.__color
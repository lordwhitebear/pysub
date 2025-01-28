import pygame

class Player:
    __slots__ = ["__transform", "__image", "__color"]
    def __init__(self, transform=(100, 100, 50, 50), image=None, color=(255, 255, 255)):
        self.__transform = transform
        self.__image = image
        self.__color = color

    def set_transform(self, transform):
        self.__transform = transform

    def get_transform(self):
        return self.__transform
    
    def get_image(self):
        return self.__image
    
    def get_color(self):
        return self.__color
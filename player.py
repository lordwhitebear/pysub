import pygame

class Player:
    def __init__(self, transform, image=None, color=(255, 255, 255)):
        self.transform = transform
        self.image = image
        self.color = color

    def set_transform(self, transform):
        self.transform = transform

    def get_transform(self):
        return self.transform
    
    def get_image(self):
        return self.image
    
    def get_color(self):
        return self.color
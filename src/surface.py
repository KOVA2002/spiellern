import pygame


class Surface:

    def __init__(self, position, size, owner_object):

        self.size = size
        self.position = position
        self.owner_object = owner_object
        self.rect = pygame.Rect(position, size)

    def update_position(self, x, y):

        self.x = x
        self.y = y

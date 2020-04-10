import pygame


class Rect(object):

    def __init__(self, posx, posy, width):
        self._rect = pygame.Rect(posx, posy, width, width)
        self._direction = None

    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction

    def get_x(self):
        return self._rect.x

    def get_y(self):
        return self._rect.y

    def get_object(self):
        return self._rect

import pygame

from menu import Menu
from game import Game

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((640, 480))
    window.fill([255, 255, 255])
    
    game = Game(window)
    game.loop()

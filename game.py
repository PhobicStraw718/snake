import pygame

import random

from rect import Rect


class Game(object):
    def __init__(self, window):
        self.window = window
        self.done = False
        self.direction = None

        self.time = 50

        self.counter = -1

        posx = random.randrange(0, 64, 2) * 10
        posy = random.randrange(0, 48, 2) * 10

        self.list_of_rect = [Rect(posx, posy, 20)]
        self.apple = self.spawn_apple()

    def add_rect(self):
        last_rect = self.list_of_rect[-1]
        if last_rect.get_direction() == pygame.K_w:
            self.list_of_rect.append(Rect(last_rect.get_x(), last_rect.get_y() + 20, 20))
        elif last_rect.get_direction() == pygame.K_s:
            self.list_of_rect.append(Rect(last_rect.get_x(), last_rect.get_y() - 20, 20))
        elif last_rect.get_direction() == pygame.K_a:
            self.list_of_rect.append(Rect(last_rect.get_x() + 20, last_rect.get_y(), 20))
        elif last_rect.get_direction() == pygame.K_d:
            self.list_of_rect.append(Rect(last_rect.get_x() - 20, last_rect.get_y(), 20))

    def spawn_apple(self):
        self.counter += 1
        posx, posy = 0, 0

        while posx == 0 or posy == 0:
            posx = random.randrange(0, 64, 2) * 10
            posy = random.randrange(0, 48, 2) * 10
            for rect in self.list_of_rect:
                if rect.get_x() == posx and posy == rect.get_y():
                    posx, posy = 0, 0
                    continue

        return pygame.Rect(posx, posy, 20, 20)

    def move(self):
        if self.direction in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
            length = len(self.list_of_rect)
            for i in range(1, length):
                self.list_of_rect[length-i].set_direction(self.list_of_rect[length-i-1].get_direction())

            self.list_of_rect[0].set_direction(self.direction)

        for rect in self.list_of_rect:
            self.move_rect(rect)

        self.check_collisions()

    def move_rect(self, rect):
        if rect.get_direction() == pygame.K_w:
            rect.get_object().move_ip(0, -20)
        elif rect.get_direction() == pygame.K_s:
            rect.get_object().move_ip(0, 20)
        elif rect.get_direction() == pygame.K_a:
            rect.get_object().move_ip(-20, 0)
        elif rect.get_direction() == pygame.K_d:
            rect.get_object().move_ip(20, 0)

    def check_collisions(self):
        first_rect = self.list_of_rect[0]

        if first_rect.get_x() == self.apple.x and first_rect.get_y() == self.apple.y:
            self.apple = self.spawn_apple()
            self.add_rect()

        for i in range(1, len(self.list_of_rect)):
            if first_rect.get_x() == self.list_of_rect[i].get_x():
                if first_rect.get_y() == self.list_of_rect[i].get_y():
                    self.done = True
                    return

        if 620 >= first_rect.get_x() >= 0 and 460 >= first_rect.get_y() >= 0:
            return

        self.done = True

    def draw(self):
        self.window.fill([255, 255, 255])
        pygame.draw.rect(self.window, (255, 0, 0), self.apple)

        for rect in self.list_of_rect:
            pygame.draw.rect(self.window, (0, 0, 0), rect.get_object())

        pygame.display.update()

    def loop(self):
        while not self.done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    self.direction = event.key

            if self.counter > 10:
                self.time -= 10
            if self.counter > 20:
                self.time -= 10

            self.move()
            self.draw()
            pygame.time.wait(self.time)

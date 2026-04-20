import random
import pygame
from pygame import Surface

from code.Entity import Entity


class Food(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.position = None
        self.size = 20
        self.image = pygame.image.load('asset/apple.png')

    def move(self):
        pass

    def spawn(self, grid_width, grid_height, snake_body=None):
        while True:
            x = random.randint(0, grid_width - 1)
            y = random.randint(0, grid_height - 1)
            new_position = (x, y)

            if snake_body is None or new_position not in snake_body:
                self.position = new_position
                break

    def draw(self, window):
        x, y = self.position
        window.blit(self.image, (x * self.size, y * self.size))
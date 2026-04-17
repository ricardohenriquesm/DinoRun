import random
import pygame
from pygame import Surface

from code.Entity import Entity


class Food(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.size = 20  # Mesmo tamanho da cobra
        self.image = pygame.image.load('asset/apple.png')  # Ajuste o caminho se necessário

    def move(self):
        pass

    def spawn(self, grid_width, grid_height, snake_body=None):
        """
        Gera uma posição aleatória para a maçã
        grid_width: largura da tela em células (ex: 400/20 = 20)
        grid_height: altura da tela em células (ex: 400/20 = 20)
        snake_body: lista com as posições do corpo da cobra (opcional)
        """
        while True:
            # Gera posição aleatória
            x = random.randint(0, grid_width - 1)
            y = random.randint(0, grid_height - 1)
            new_position = (x, y)

            # Se passar o corpo da cobra, verifica se não spawna em cima dela
            if snake_body is None or new_position not in snake_body:
                self.position = new_position
                break

    def draw(self, window):
        x, y = self.position
        window.blit(self.image, (x * self.size, y * self.size))
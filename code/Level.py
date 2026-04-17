#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code.Const import EVENT_APPLE, SPAWN_TIME, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('bgsnake'))
        self.snake = EntityFactory.get_entity('snake')
        self.entity_list.append(self.snake)

        # Configurações do grid
        self.grid_width = WIN_WIDTH // 20
        self.grid_height = WIN_HEIGHT // 20

        # Criar a primeira maçã
        self.apple = EntityFactory.get_entity('apple')
        self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)
        self.entity_list.append(self.apple)

    def reset_game(self):
        """Reinicia o jogo"""
        self.entity_list.clear()
        self.entity_list.append(EntityFactory.get_entity('bgsnake'))
        self.snake = EntityFactory.get_entity('snake')
        self.entity_list.append(self.snake)

        self.apple = EntityFactory.get_entity('apple')
        self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)
        self.entity_list.append(self.apple)

    def check_apple_collision(self):
        """Verifica colisão com a maçã usando uma área maior"""
        head_x, head_y = self.snake.body[0]
        apple_x, apple_y = self.apple.position

        # Converte posição de grid para pixels
        head_pixel_x = head_x * 20
        head_pixel_y = head_y * 20
        apple_pixel_x = apple_x * 20
        apple_pixel_y = apple_y * 20

        # Cria retângulos de colisão
        # Cabeça da cobra (20x20)
        head_rect = pygame.Rect(head_pixel_x, head_pixel_y, 20, 20)

        # Maçã com área maior (25x25 centralizada = +2.5 pixels em cada lado)
        apple_rect = pygame.Rect(apple_pixel_x - 2, apple_pixel_y - 2, 24, 24)

        # Verifica se os retângulos colidem
        return head_rect.colliderect(apple_rect)

    def run(self):
        clock = pygame.time.Clock()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'

                    # CONTROLE DA COBRA
                    if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.direction = "RIGHT"

            self.window.fill((0, 0, 0))
            clock.tick(10)

            # Mover entidades
            for ent in self.entity_list:
                ent.move()

            # VERIFICAR COLISÃO COM PAREDE
            if self.snake.check_wall_collision(self.grid_width, self.grid_height):
                print("Game Over - Bateu na parede!")
                pygame.time.delay(500)
                self.reset_game()

            # VERIFICAR COLISÃO CONSIGO MESMA
            if self.snake.check_self_collision():
                print("Game Over - Bateu em si mesma!")
                pygame.time.delay(500)
                self.reset_game()

            # VERIFICAR COLISÃO COM MAÇÃ (usando o novo método)
            if self.check_apple_collision():
                self.snake.grow = True
                self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)

            # Desenhar tudo
            for ent in self.entity_list:
                ent.draw(self.window)

            pygame.display.update()
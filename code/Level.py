#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, C_WHITE
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

        self.grid_width = WIN_WIDTH // 20
        self.grid_height = WIN_HEIGHT // 20
        self.total_cells = self.grid_width * self.grid_height
        self.victory_threshold = self.total_cells * 0.5  # precisa ocupar 50% pra ganhar

        self.apple = EntityFactory.get_entity('apple')
        self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)
        self.entity_list.append(self.apple)

    def reset_game(self):
        self.entity_list.clear()
        self.entity_list.append(EntityFactory.get_entity('bgsnake'))
        self.snake = EntityFactory.get_entity('snake')
        self.entity_list.append(self.snake)

        self.apple = EntityFactory.get_entity('apple')
        self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)
        self.entity_list.append(self.apple)

    def colisao_maca(self):
        head_x, head_y = self.snake.body[0]
        apple_x, apple_y = self.apple.position

        head_pixel_x = head_x * 20
        head_pixel_y = head_y * 20
        apple_pixel_x = apple_x * 20
        apple_pixel_y = apple_y * 20

        head_rect = pygame.Rect(head_pixel_x, head_pixel_y, 20, 20)
        apple_rect = pygame.Rect(apple_pixel_x - 2, apple_pixel_y - 2, 24, 24)

        return head_rect.colliderect(apple_rect)

    def ganhou(self):
        tamanho = len(self.snake.body)
        if tamanho >= self.victory_threshold:
            return True
        else:
            return False

    def tela_vitoria(self):
        font_grande = pygame.font.SysFont(name="Lucida Sans Typewriter", size=60)
        font_pequena = pygame.font.SysFont(name="Lucida Sans Typewriter", size=20)

        overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.window.blit(overlay, (0, 0))

        txt_vitoria = font_grande.render("VITORIA!", True, C_ORANGE)
        rect_vitoria = txt_vitoria.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))
        self.window.blit(txt_vitoria, rect_vitoria)

        tamanho_cobra = len(self.snake.body)
        porcentagem = (tamanho_cobra / self.total_cells) * 100
        txt_stats = font_pequena.render(f"Voce ocupou {porcentagem:.1f}% do mapa!", True, C_WHITE)
        rect_stats = txt_stats.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 20))
        self.window.blit(txt_stats, rect_stats)

        txt_instrucao = font_pequena.render("Pressione SPACE para reiniciar", True, C_WHITE)
        rect_instrucao = txt_instrucao.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 60))
        self.window.blit(txt_instrucao, rect_instrucao)

        txt_instrucao2 = font_pequena.render("ou ESC para voltar ao menu", True, C_WHITE)
        rect_instrucao2 = txt_instrucao2.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 90))
        self.window.blit(txt_instrucao2, rect_instrucao2)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        return 'continue'
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'

    def run(self):
        pygame.mixer_music.load('./asset/levelsnake.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'

                    # controles da cobra
                    if event.key == pygame.K_UP:
                        if self.snake.direction != "DOWN":
                            self.snake.direction = "UP"
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction != "UP":
                            self.snake.direction = "DOWN"
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction != "RIGHT":
                            self.snake.direction = "LEFT"
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction != "LEFT":
                            self.snake.direction = "RIGHT"

            self.window.fill((0, 0, 0))
            clock.tick(10)

            for ent in self.entity_list:
                ent.move()

            if self.snake.check_wall_collision(self.grid_width, self.grid_height):
                print("Game Over - Bateu na parede!")
                pygame.time.delay(500)
                self.reset_game()

            if self.snake.check_self_collision():
                print("Game Over - Bateu em si mesma!")
                pygame.time.delay(500)
                self.reset_game()

            if self.colisao_maca():
                self.snake.grow = True
                self.apple.spawn(self.grid_width, self.grid_height, self.snake.body)

            if self.ganhou():
                print(f"VITORIA! A cobra ocupou {len(self.snake.body)} de {self.total_cells} celulas!")
                for ent in self.entity_list:
                    ent.draw(self.window)
                pygame.display.update()

                resultado = self.tela_vitoria()
                if resultado == 'quit':
                    return 'quit'
                elif resultado == 'menu':
                    return 'menu'

            for ent in self.entity_list:
                ent.draw(self.window)

            pygame.display.update()
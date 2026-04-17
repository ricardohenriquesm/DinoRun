#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menusnake.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        menu_option = 1
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, text="SNAKE", text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(50, text="GAME", text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))
            self.menu_text(20, text="PLAY", text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 200 + 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 'playing'
                    if event.key == pygame.K_ESCAPE:
                        return 'quit'

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

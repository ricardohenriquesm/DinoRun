#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code.Const import EVENT_APPLE, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('bgsnake'))
        snake = EntityFactory.get_entity('snake')
        self.entity_list.append(snake)
        pygame.time.set_timer(EVENT_APPLE, SPAWN_TIME)

    def run(self):
        clock = pygame.time.Clock()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'
            self.window.fill((0, 0, 0))
            clock.tick(10)
            for ent in self.entity_list:
                ent.move()
                ent.draw(self.window)

            pygame.display.update()




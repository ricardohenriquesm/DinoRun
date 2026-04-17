#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        pass

    def draw(self, window):
        if self.surf and self.rect:
            window.blit(self.surf, self.rect)

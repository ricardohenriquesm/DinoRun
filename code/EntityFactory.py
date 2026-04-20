#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import abstractmethod

from code.Background import Background
from code.Snake import Snake
from code.Food import Food


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'bgsnake':
                return Background('bgsnake', position=(0, 0))

            case 'snake':
                return Snake('snake', position=(1, 1))

            case 'apple':
                return Food('apple', position=(0, 0))
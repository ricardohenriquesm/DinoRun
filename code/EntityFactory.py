#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import abstractmethod


class EntityFactory:
    def __init__(self):
        pass

    @abstractmethod
    def get_entity(entity_name: str):
        pass

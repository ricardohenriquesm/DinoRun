import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.state = 'menu'

        self.menu = Menu(self.window)
        self.level = None

    def run(self):
        while True:
            if self.state == 'menu':
                self.state = self.menu.run()

            elif self.state == 'playing':
                if self.level is None:
                    self.level = Level(self.window, 'level')

                self.state = self.level.run()

            elif self.state == 'quit':
                return False




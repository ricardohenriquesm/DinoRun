import pygame
from code.Entity import Entity


class Snake(Entity):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position
        self.body = [
            (8, 5),
            (7, 5),
            (6, 5),
            (5, 5),
            (4, 5),
            (3, 5)
            ]
        self.direction = "RIGHT"
        self.grow = False

        self.size = 20

        # HEAD
        self.head_up = pygame.image.load('asset/head_up.png')
        self.head_down = pygame.image.load('asset/head_down.png')
        self.head_left = pygame.image.load('asset/head_left.png')
        self.head_right = pygame.image.load('asset/head_right.png')

        # TAIL
        self.tail_up = pygame.image.load('asset/tail_up.png')
        self.tail_down = pygame.image.load('asset/tail_down.png')
        self.tail_left = pygame.image.load('asset/tail_left.png')
        self.tail_right = pygame.image.load('asset/tail_right.png')

        # BODY
        self.body_horizontal = pygame.image.load('asset/body_horizontal.png')
        self.body_vertical = pygame.image.load('asset/body_vertical.png')

        # CURVAS
        self.body_topleft = pygame.image.load('asset/body_topleft.png')
        self.body_topright = pygame.image.load('asset/body_topright.png')
        self.body_bottomleft = pygame.image.load('asset/body_bottomleft.png')
        self.body_bottomright = pygame.image.load('asset/body_bottomright.png')

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def check_self_collision(self):
        """Verifica se a cabeça colidiu com o próprio corpo"""
        head = self.body[0]
        return head in self.body[1:]  # Verifica se a cabeça está em qualquer parte do corpo

    def check_wall_collision(self, grid_width, grid_height):
        """Verifica se a cobra bateu na parede"""
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height

    def draw(self, window):
        for i in range(len(self.body)):
            x, y = self.body[i]

            # CABEÇA
            if i == 0:
                next_x, next_y = self.body[i + 1]

                dx = x - next_x
                dy = y - next_y

                if dx == 1:
                    image = self.head_right
                elif dx == -1:
                    image = self.head_left
                elif dy == 1:
                    image = self.head_down
                elif dy == -1:
                    image = self.head_up

            # CAUDA
            elif i == len(self.body) - 1:
                prev_x, prev_y = self.body[i - 1]

                dx = x - prev_x
                dy = y - prev_y

                if dx == 1:
                    image = self.tail_right
                elif dx == -1:
                    image = self.tail_left
                elif dy == 1:
                    image = self.tail_down
                elif dy == -1:
                    image = self.tail_up

            # CORPO
            else:
                prev_x, prev_y = self.body[i - 1]
                next_x, next_y = self.body[i + 1]

                dx1 = x - prev_x
                dy1 = y - prev_y

                dx2 = x - next_x
                dy2 = y - next_y

                # RETO
                if dx1 == dx2:
                    image = self.body_horizontal
                elif dy1 == dy2:
                    image = self.body_vertical

                # CURVAS
                else:
                    if (dx1 == 1 and dy2 == 1) or (dy1 == 1 and dx2 == 1):
                        image = self.body_bottomright
                    elif (dx1 == -1 and dy2 == 1) or (dy1 == 1 and dx2 == -1):
                        image = self.body_bottomleft
                    elif (dx1 == 1 and dy2 == -1) or (dy1 == -1 and dx2 == 1):
                        image = self.body_topright
                    elif (dx1 == -1 and dy2 == -1) or (dy1 == -1 and dx2 == -1):
                        image = self.body_topleft

            window.blit(image, (x * self.size, y * self.size))
import pygame
import random
from pygame.locals import *


class ScreenInfo:
    def __init__(self, width: int, height: int, cell_size: int, screen) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = screen
        # Width/Height cells amount
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size


class Game:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    # Draw screen lines
    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))


def get_color(param: int) -> pygame.color:
    purple = pygame.Color(116, 33, 125)  # poison
    green = pygame.Color(34, 134, 83)  # food
    blue = pygame.Color(0, 153, 153)  # resident of the cold biome
    yellow = pygame.Color(191, 153, 48)  # resident of the normal biome
    red = pygame.Color(166, 72, 0)  # resident of the warm biome
    Colors = {0: purple, 1: green, 2: blue, 3: yellow, 4: red}
    return Colors[param]


def create_grid(Inform, Map=None, randomize: bool = True) -> None:
    if Map == None:
        Map = [[0 for j in range(Inform.cell_width)] for i in range(Inform.cell_height)]
    if randomize:
        for hei in range(Inform.cell_height):
            for wei in range(Inform.cell_width):
                Map[hei][wei] = random.randint(0, 4)  # 0 - poison, 1 - food, 2 - cold, 3 - normal, 4 - warm
    for hei in range(Inform.cell_height):
        for wei in range(Inform.cell_width):
            Rect = (wei * Inform.cell_size, hei * Inform.cell_size, Inform.cell_size, Inform.cell_size)
            pygame.draw.rect(Inform.screen, get_color(Map[hei][wei]), Rect)
            # pygame.draw.rect(Inform.screen, pygame.Color("Red"), Rect)


if __name__ == '__main__':
    game = Game(600, 400, 10)
    screen = ScreenInfo(600, 400, 10, game.screen)
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Game of Life')
    game.screen.fill(pygame.Color('white'))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        game.draw_lines()
        create_grid(screen)
        # Display surface updating. We can use display.update() to update only a portion of a screen
        pygame.display.flip()
        # Limiting runtime speed of the game
        clock.tick(game.speed)
    pygame.quit()
    clock = pygame.time.Clock()

import pygame
import random
from pygame.locals import *


class Field:
    def __init__(self, width: int, height: int, cell_size: int) -> None:
        self.Width = width
        self.Height = height
        self.CellSize = cell_size

        # Создание нового окна
        pygame.display.set_caption('LifeHub')
        self.Screen = pygame.display.set_mode((width, height))

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.CellWidthAmount = self.Width // self.CellSize
        self.CellHeightAmount = self.Height // self.CellSize

    # Draw screen lines
    def draw_lines(self) -> None:
        for x in range(0, self.Width, self.CellSize):
            pygame.draw.line(self.Screen, pygame.Color('black'),
                             (x, 0), (x, self.Height))
        for y in range(0, self.Height, self.CellSize):
            pygame.draw.line(self.Screen, pygame.Color('black'),
                             (0, y), (self.Width, y))

    def create_grid(self, Map = None, randomize: bool = True) -> None:
        # handler.RunOnTick()
        if Map == None:
            Map = [[0 for j in range(self.CellWidthAmount)] for i in range(self.CellHeightAmount)]
        if randomize:
            for hei in range(self.CellHeightAmount):
                for wei in range(self.CellWidthAmount):
                    Map[hei][wei] = random.randint(0, 4)  # 0 - poison, 1 - food, 2 - cold, 3 - normal, 4 - warm
        for hei in range(self.CellHeightAmount):
            for wei in range(self.CellWidthAmount):
                Rect = (wei * self.CellSize, hei * self.CellSize, self.CellSize, self.CellSize)
                pygame.draw.rect(self.Screen, GetColor(Map[hei][wei]), Rect)
                # pygame.draw.rect(Inform.screen, pygame.Color("Red"), Rect)


def CellSize(weight: int, cells: int) -> int:
    return weight // cells


def ScreenFix(scr_param: list, cell_size: int)-> list:
    return [(scr_param[0] // cell_size) * cell_size, (scr_param[1] // cell_size) * cell_size]


def GetColor(param: int) -> pygame.color:
    purple = pygame.Color(116, 33, 125)  # poison
    green = pygame.Color(34, 134, 83)  # food
    blue = pygame.Color(0, 153, 153)  # resident of the cold biome
    yellow = pygame.Color(191, 153, 48)  # resident of the normal biome
    red = pygame.Color(166, 72, 0)  # resident of the warm biome
    Colors = {0: purple, 1: green, 2: blue, 3: yellow, 4: red}
    return Colors[param]


def StartGame(wPar, handler):
    pygame.init()
    clock = pygame.time.Clock()

    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    cell_size = CellSize(w // 2, wPar.WorldSize)
    w, h = ScreenFix([w // 2, h // 2], cell_size)

    game = Field(w, h, cell_size)
    game.Screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit(0)
        game.draw_lines()
        game.create_grid()
        # Display surface updating. We can use display.update() to update only a portion of a screen
        pygame.display.flip()
        # Limiting runtime speed of the game
        clock.tick(wPar.TickUniverse)
    pygame.quit()

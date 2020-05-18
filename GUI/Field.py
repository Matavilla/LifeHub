import pygame
import random
from pygame.locals import *


class Field:
    def __init__(self, w: int, h: int, world_size: int) -> None:
        self.LengthWindow = min((3 * w) // 4, (3 * h) // 4)
        self.LengthWindow += self.LengthWindow % world_size
        self.CellSize = self.LengthWindow // world_size
        
        pygame.display.set_caption('LifeHub')
        self.Screen = pygame.display.set_mode((self.LengthWindow, self.LengthWindow))


    def create_grid(self, Map) -> None:
        for y in range(Map.Size):
            for x in range(Map.Size):
                Rect = (x * self.CellSize, y * self.CellSize, self.CellSize, self.CellSize)
                color = pygame.Color(*(Map.Field[x][y].get_color()))
                pygame.draw.rect(self.Screen, color, Rect)
                # pygame.draw.rect(Inform.screen, pygame.Color("Red"), Rect)


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
    game = Field(w, h, wPar.WorldSize)

    game.Screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit(0)
        # handler.RunOnTick()
        game.create_grid(handler.Map)
        pygame.display.flip()
        clock.tick(wPar.TickUniverse)
    pygame.quit()

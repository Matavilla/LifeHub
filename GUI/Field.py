import pygame
import random
from random import randint
import sys
from pygame.locals import *


class Field:
    '''Отрисовка карты и объектов'''
    def __init__(self, 
                caption: str,
                width: int, 
                height: int, 
                back_image_filename: str) -> None:
        self.Width = width
        self.Height = height
        self.BackgroundImage = pygame.image.load(back_image_filename)
        # Создание нового окна
        pygame.display.set_caption(caption)
        self.Screen = pygame.display.set_mode((width, height))

    def draw_map(self, map_):
        self.Screen.blit(self.BackgroundImage, (0, 0))
        for objects in map_:
            for obj in objects:
                if obj.Alive:
                    pygame.draw.rect(self.Screen, obj.Color, obj.Bounds)

    # def create_grid(self, Map=None, randomize: bool = True) -> None:
    #     # handler.RunOnTick()
    #     if Map == None:
    #         Map = [[0 for j in range(self.CellWidthAmount)] for i in range(self.CellHeightAmount)]
    #     if randomize:
    #         for hei in range(self.CellHeightAmount):
    #             for wei in range(self.CellWidthAmount):
    #                 Map[hei][wei] = random.randint(0, 4)  # 0 - poison, 1 - food, 2 - cold, 3 - normal, 4 - warm
    #     for hei in range(self.CellHeightAmount):
    #         for wei in range(self.CellWidthAmount):
    #             Rect = (wei * self.CellSize, hei * self.CellSize, self.CellSize, self.CellSize)
    #             pygame.draw.rect(self.Screen, get_color(Map[hei][wei]), Rect)
                # pygame.draw.rect(Inform.screen, pygame.Color("Red"), Rect)


# def get_color(param: int) -> pygame.color:
#     purple = pygame.Color(116, 33, 125)  # poison
#     green = pygame.Color(34, 134, 83)  # food
#     blue = pygame.Color(0, 153, 153)  # resident of the cold biome
#     yellow = pygame.Color(191, 153, 48)  # resident of the normal biome
#     red = pygame.Color(166, 72, 0)  # resident of the warm biome
#     Colors = {0: purple, 1: green, 2: blue, 3: yellow, 4: red}
#     return Colors[param]


def StartGame(wPar, handler):
    pygame.init()
    clock = pygame.time.Clock()
    # w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    # w, h = w // 2, h // 2
    background_image = 'images/background.png'

    field = Field('LifeHub', 800, 800, background_image)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit(0)
        # Display surface updating. We can use display.update() to update only a portion of a screen
        handler_map = handler.run_on_tick()
        field.draw_map(handler_map)
        pygame.display.update()
        # Limiting runtime speed of the game
        clock.tick(wPar.TickUniverse)
    pygame.quit()

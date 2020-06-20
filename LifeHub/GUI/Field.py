"""
Данный модуль осуществляет отрисовку карты вселенной на каждый тик вселенной,
предварительно вызывая обработчик.
"""

import pygame
import os

class Field:
    """ Класс, который выводит игровое поле в окно.
    """
    def __init__(self, w: int, h: int, world_size: int) -> None:
        self.LengthWindow = min((3 * w) // 4, (3 * h) // 4)
        self.LengthWindow -= self.LengthWindow % world_size
        self.CellSize = self.LengthWindow // world_size
        pygame.display.set_caption('LifeHub')
        self.Screen = pygame.display.set_mode((self.LengthWindow,
                                               self.LengthWindow))

    def create_grid(self, Map) -> None:
        """ Функция, выводящая игровое поле в окно.

        :param Map: Игровое поле.
        """
        for y in range(Map.Size):
            for x in range(Map.Size):
                Rect = (x * self.CellSize, y * self.CellSize,
                        self.CellSize, self.CellSize)
                color = pygame.Color(*(Map.Field[x][y].get_color()))
                pygame.draw.rect(self.Screen, color, Rect)


def StartGame(handler):
    """ Класс, создающий окно.

    :param handler: Обработчик вселенной.
    """
    pygame.init()
    Path = os.path.dirname(os.path.abspath(__file__))
    pygame.mixer.music.load(Path+'/../../Sounds/Test.wav')
   
    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    game = Field(w, h, handler.World_par.WorldSize)

    game.Screen.fill(pygame.Color('white'))

    running = True
    tick = handler.World_par.TickUniverse
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tick += int(tick * 0.2) + 1
                elif event.key == pygame.K_DOWN:
                    tick -= int(tick * 0.3)
        handler.RunOnTick()
        game.create_grid(handler.Map)
        pygame.display.flip()
        clock.tick(tick)
    pygame.quit()

import pygame
import random
from random import randint
import sys
from pygame.locals import *


class Bot:
    def __init__(self, x: int, y: int, 
                       cell_size: int, 
                       size: int, 
                       color: tuple, 
                       speed: int, 
                       alive: bool = True) -> None:
        self.Bounds = pygame.Rect(x, y, size*cell_size,  size*cell_size)
        self.x = x
        self.y = y
        self.CellSize = cell_size
        self.Size = size
        self.Color = color
        self.Speed = speed
        self.Alive = alive
        #self.sensity = ...
        #self.agression = ...
        #...

    def draw(self, screen):
        pygame.draw.rect(screen, self.Color, self.Bounds)


    def move(self, dx: int, dy: int) -> None:
        #self.bounds = pygame.Rect(self.x + dx, self.y + dy, self.w, self.h)
        self.Bounds = self.Bounds.move(dx, dy)

    def update(self):
        """"""
        if self.Speed == 0:
            return

        dx, dy = 0, 0
        vert = self.Speed*self.CellSize
        hor = self.Speed*self.CellSize
        direction = randint(1,5)
        
        if direction == 1:
            dx, dy = -hor, 0
        elif direction == 2:
            dx, dy = 0, -vert
        elif direction == 3:
            dx, dy = hor, 0
        elif direction == 4:
            dx, dy = 0, vert

        self.move(dx, dy)



#Class Game will be deleted. Its temporary solve for testing
class Game:
    def __init__(self, width: int, 
                       height: int, 
                       cell_size: int, 
                       back_image_filename: str,
                       tik: int) -> None:
        self.Width = width
        self.Height = height
        self.CellSize = cell_size
        self.BackgroundImage = pygame.image.load(back_image_filename)
        self.Objects = []
        self.GameOver = False
        self.Tik = tik
        pygame.init()

        # Создание нового окна
        pygame.display.set_caption('LifeHub')
        self.Screen = pygame.display.set_mode((width, height))

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.CellWidthAmount = self.Width // self.CellSize
        self.CellHeightAmount = self.Height // self.CellSize
        self.clock = pygame.time.Clock()

    # Draw screen lines
    def draw_lines(self) -> None:
        step = self.Height//3
        pygame.draw.line(self.Screen, (0,0,0), (0, step), (self.Width, step))
        pygame.draw.line(self.Screen, (0,0,0), (0, 2*step), (self.Width, 2*step))
        # for x in range(0, self.Width, self.CellSize):
        #     pygame.draw.line(self.Screen, pygame.Color('black'),
        #                      (x, 0), (x, self.Height))
        # for y in range(0, self.Height, self.CellSize):
        #     pygame.draw.line(self.Screen, pygame.Color('black'),
        #                      (0, y), (self.Width, y))

    def update_objects(self):
        for o in self.Objects:
            o.update()


    def draw_objects(self):
        for o in self.Objects:
            o.draw(self.Screen)


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

    def run(self):
        while not self.GameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.Screen.blit(self.BackgroundImage, (0, 0))
            self.draw_lines()
            #self.handle_events()
            self.update_objects()
            self.draw_objects()
            pygame.display.update()
            self.clock.tick(self.Tik)



class Lifehub(Game):
    def __init__(self, width: int, 
                       height: int, 
                       cell_size: int, 
                       back_image_filename: str,
                       tik: int) -> None:
        Game.__init__(self, width, height, cell_size, back_image_filename, tik)
        self.bot = None
        self.create_objects()

    def create_objects(self):
        self.create_bot()


    def create_bot(self):
        speed = 1

        self.bot = Bot(self.Width // 2,
                         self.Height // 2,
                         self.CellSize,
                         1,
                         (255,0,0),
                         speed)
        self.Objects.append(self.bot)

        self.bot = Bot(self.Width // 4,
                         self.Height // 2,
                         self.CellSize,
                         2,
                         (255,0,0),
                         speed+1)
        self.Objects.append(self.bot)

        self.bot = Bot(self.Width // 2,
                         self.Height // 4,
                         self.CellSize,
                         1,
                         (255,0,0),
                         speed+2)
        self.Objects.append(self.bot)


    def update(self):
        super().update()



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
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    w, h = w // 2, h // 2
    background_image = 'images/background.png'

    Lifehub(w, h, 10, background_image, wPar.TickUniverse).run()
    # game = Game(w, h, 10)
    # #game.Screen.fill(pygame.Color('white'))

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             raise SystemExit(0)
    #     game.draw_lines()
    #     game.create_grid()
    #     # Display surface updating. We can use display.update() to update only a portion of a screen
    #     pygame.display.flip()
    #     # Limiting runtime speed of the game
    #     clock.tick(wPar.TickUniverse)
    # pygame.quit()

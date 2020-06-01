import pygame
from random import randint
from src.cell import Cell


class Bot(Cell):
    def __init__(self, x: int=0, y: int=0, 
                cell_size: int=0, 
                size: int=0, 
                color: tuple=(0,0,0), 
                speed: int=0, 
                alive: bool=True) -> None:
        Cell.__init__(self, x, y, cell_size, alive)
        self.Size = size
        self.Color = color
        self.Speed = speed
        self.Alive = alive
        self.Sensity = 1
        self.Agression = 10
        self.Life = 100
        #...

    def random_move(self, map_, x, y):
        #bot = map_[x][y]
        #cell_size = self.CellSize
        cells_per_row = len(map_[0])
        cells_per_coll = len(map_)
        if self.Speed == 0:
            return
        dx, dy = 0, 0
        vert = self.Speed
        hor = self.Speed
        direction = randint(1,8)
        if direction == 1:
            dx, dy = -hor, vert
        elif direction == 2:
            dx, dy = 0, vert
        elif direction == 3:
            dx, dy = hor, vert
        elif direction == 4:
            dx, dy = hor, 0
        elif direction == 5:
            dx, dy = hor, -vert
        elif direction == 6:
            dx, dy = 0, -vert
        elif direction == 7:
            dx, dy = -hor, -vert
        elif direction == 8:
            dx, dy = -hor, 0

        if x + dx >= cells_per_row or x + dx < 0:
            dx = 0

        if y + dy >= cells_per_coll or y + dy < 0:
            dy = 0

        #return dx, dy

        self.Bounds = pygame.Rect((x + dx) * self.CellSize, (y + dy) * self.CellSize,\
                                  self.CellSize, self.CellSize)
        self.X = (x + dx) * self.CellSize
        self.Y = (y + dy) * self.CellSize
        map_[x + dx][y + dy] = self
        map_[x + dx][y + dy].WasChecked = True
        if dx != 0 or dy != 0:
            map_[x][y] = Cell(x * self.CellSize, y * self.CellSize, self.CellSize)

    def action_on_tick(self, map_, x, y):
        #self.check_around(self, map_, x, y)
        self.random_move(map_, x, y)

    # def check_around(self, map_, x, y):
    #     for i in range(1, self.Sensity + 1):








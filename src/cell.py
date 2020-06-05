import pygame

class Cell:
    def __init__(self, x: int, y: int, 
                cell_size: int, alive: bool=False) -> None:
        self.Bounds = pygame.Rect(x, y, cell_size, cell_size)
        self.X = x
        self.Y = y
        self.CellSize = cell_size
        self.Alive = alive
        self.WasChecked = False

    def action_on_tick(self):
    	pass
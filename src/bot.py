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
        #self.sensity = ...
        #self.agression = ...
        #...
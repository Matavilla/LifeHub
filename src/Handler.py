import random

import src.map as map
import src.food as food

class Handler:   
    def __init__(self, worldPar):
        self.World_par = worldPar
        self.Map = None
        self.Tick = 1

    def create_map(self):
        self.Map = map.Map(self.World_par.WorldSize)
        self.Map.generate()

    def create_world(self):
        self.create_map()

        count = self.World_par.NumBots1 // 2
        self.spawn_food(1, count)

        count = self.World_par.NumBots2 // 2
        self.spawn_food(2, count)

        count = self.World_par.NumBots3 // 2 
        self.spawn_food(3, count)
#+ bot

    def spawn_food(self, biom, count):
        while count:
            x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_food(food.Food(biom))
            count -= 1


    def RunOnTick(self):
        '''Готовит изображение для вывода'''
           
        if not self.Tick % self.World_par.T_1:
            count = 1
            self.spawn_food(1, count)

        if not self.Tick % self.World_par.T_2:
            count = 2
            self.spawn_food(2, count)

        if not self.Tick % self.World_par.T_3:
            count = 3
            self.spawn_food(3, count)

        self.Tick += 1

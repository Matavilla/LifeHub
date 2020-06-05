import random

class Food:
    Biom_food_bound = {1 : (0, 40), 2 : (0, 70), 3 : (0, 100)}
    Biom_toxic_bound = {1 : (0, 20), 2 : (0, 40), 3 : (0, 100)}

    def __init__(self, biom):
        self.Food_value = random.randint(*self.Biom_food_bound[biom])
        self.Toxic_value = random.randint(*self.Biom_toxic_bound[biom])
        self.set_color()

    def set_color(self):
        self.Color = ((self.Toxic_value * 3) % 256, (self.Food_value * 4) % 256, 0)

import random

class Food:
    Biom_food_bound = {1 : (0, 40), 2 : (0, 70), 3 : (0, 100)}
    Biom_toxic_bound = {1 : (0, 20), 2 : (0, 40), 3 : (0, 100)}

    def __init__(self, biom):
        self.food_value = random.randint(*self.Biom_food_bound[biom])
        self.toxic_value = random.randint(*self.Biom_toxic_bound[biom])
        self.set_color()

    def set_color(self):
        self.color = (self.toxic_value % 41, self.food_value % 41 ,0)

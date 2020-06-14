"""
Модуль, который описывает объект вселенной - еда. Еда имеет показатели
питательности и ядовитости, в зависимости от которых бот либо получает
либо теряет здоровье.
"""

import random


class Food:
    """ Класс, описывающий еду ботов.
    """
    def __init__(self, biom):
        biom_food_bound = {1: (0, 200), 2: (0, 100), 3: (0, 30)}
        biom_toxic_bound = {1: (0, 30), 2: (0, 100), 3: (0, 200)}

        self.Food_value = random.randint(*biom_food_bound[biom])
        self.Toxic_value = random.randint(*biom_toxic_bound[biom])
        self.set_color()

    def set_color(self):
        red, green = 0, 0
        if self.Toxic_value < 50:
            red = 60
        elif self.Toxic_value < 100:
            red = 150
        else:
            red = 255
        if self.Food_value < 50:
            green = 60
        elif self.Food_value < 100:
            green = 150
        else:
            green = 255
        self.Color = (red, green, 0)

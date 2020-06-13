import random


class Food:
    """ Объект мира который может быть поглащен ботами.
    Каждая яда содержит в себе питательность и ядовитость.

    Biom_food_bound - питательная ценность еды в каждом из биомов.

    Biom_toxic_bound - ядовитость еды в каждом из биомов.

    """
    Biom_food_bound = {1: (0, 200), 2: (0, 100), 3: (0, 30)}
    Biom_toxic_bound = {1: (0, 30), 2: (0, 100), 3: (0, 200)}

    def __init__(self, biom):
        self.Food_value = random.randint(*self.Biom_food_bound[biom])
        self.Toxic_value = random.randint(*self.Biom_toxic_bound[biom])
        self.set_color()

    def set_color(self):
        """ Устанавливает цвет еды

        :return: Цвет еды
        """
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

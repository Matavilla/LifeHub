"""
Данный модуль содержит класс, описывающий карту игрового поля, а также класс,
из объектов которого состоит карта. Объектами карты могут быть: бот, еда или
пустая ячейка, которая соответствует определенному биому.
"""

import random


class MapCell:
    """ Класс, описывающий клетку игрового поля.
    """    
    def __init__(self, num_biom):
        self.Biom = num_biom
        self.Bot_ref = None
        self.Food_ref = None

    def get_color(self):
        biom_color = {1: (102, 205, 170),
                      2: (152, 251, 152),
                      3: (255, 222, 173)}
        if self.is_bot_here():
            return self.Bot_ref.color()
        if self.is_food_here():
            return self.Food_ref.Color
        return biom_color[self.Biom]

    def set_bot(self, bot):
        self.Bot_ref = bot

    def set_food(self, food):
        self.Food_ref = food

    def is_bot_here(self):
        return self.Bot_ref

    def is_food_here(self):
        return self.Food_ref


class Map:
    """ Класс, описывающий карту игрового поля.
    """
    def __init__(self, size):
        self.Size = size
        self.Field = [[None for x in range(size)] for y in range(size)]
        self.Biom_coord = [[], [], []]

    def clear(self):
        for line in self.Field:
            for cell in line:
                cell.Bot_ref = None
                cell.Food_ref = None

    def generate(self):
        """Функция, генерирующая карту игрового поля.
        """
        REGULARITY_CELL = 2
        dx1, dx2 = 0, 0
        bound1 = random.randint(self.Size // 4, self.Size // 3)
        bound2 = random.randint((2 * self.Size) // 3, (3 * self.Size) // 4)
        reg = REGULARITY_CELL
        smoothing = True
        for x in range(self.Size):
            biom = 1
            for y in range(self.Size):
                if y == bound1:
                    biom += 1
                if y == bound2:
                    biom += 1
                self.Biom_coord[biom - 1].append((x, y))
                self.Field[x][y] = MapCell(biom)
            if not reg:
                if smoothing:
                    smoothing = False
                    dx1, dx2 = 0, 0
                    reg += 1
                else:
                    smoothing = True
                    dx1, dx2 = random.randint(0, 100), random.randint(0, 100)
                    dx1 = 1 if dx1 > 66 else 0 if dx1 > 33 else -1
                    dx2 = 1 if dx2 > 66 else 0 if dx2 > 33 else -1
                    reg = REGULARITY_CELL
            if bound2 - bound1 < 5:
                dx1 *= -1
                dx2 += -1
            bound1 += dx1
            bound2 += dx2
            reg -= 1
        random.shuffle(self.Biom_coord[0])
        random.shuffle(self.Biom_coord[1])
        random.shuffle(self.Biom_coord[2])

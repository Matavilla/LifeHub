import random
import array
import src.dna as dna


class Bot:
    """
        Объект вселенной с искусственным интеллектом и ДНК
        Значения бота:

        Curr_direction:

        0 -> up + left

        1 -> up

        2 -> up + right

        ...

        Pointer_of_ai - указатель на текущую команду ИИ.

        Life - текущее количество жизней.

        TimeSpeed - количество тиков за одно действие.

        :param biom: номер биома
        :type biom: int


        """
    Biom_bot_color = {1: (0, 0, 255),
                      2: (255, 255, 224),
                      3: (255, 0, 255)}

    Bias_dir = [(-1, -1), (0, -1), (1, -1), (1, 0),
                (1, 1), (0, 1), (-1, 1), (-1, 0)]

    def __init__(self, biom):
        self.Dna = dna.Dna(biom)
        self.Ai = AI()
        self.Curr_direction = random.randint(0, 7)
        self.Pointer_of_ai = 0
        self.Life = 300
        self.DeathTick = 0
        self.Age = 0
        # amount of ticks for one move
        self.TimeSpeed = 5 - (self.Dna.get("speed") // 52)

    def color(self):
        """ Получить цвет бота

        :return: Новый цвет
        """
        return self.Biom_bot_color[self.Dna.Biom]

    def get_dir_and_action(self, x, y, map_):
        """ Определяет действие бота и его дальнейшее направления
        Команды:

        0..39 - move

        40..79 - attack or catch

        80..119 - check

        120..159 - rotate

        160..255 - jump

        :param x: координата бота по оси x
        :type x: int
        :param y: координата бота по оси y
        :type y: int
        :param map_: Карта вселенной
        :type map_: Map from map.Map.py

        :return:
        dx - смещение бота на карте по x координате.
        dy - смещение бота на карте по y координате.
        action - действие (move/attack).
        """
        curr_command = self.Ai.Gens[self.Pointer_of_ai]
        dx, dy, action = 0, 0, None
        max_num_of_actions = 10
        while 80 <= curr_command <= 255 and max_num_of_actions:
            num_bias_dir = (curr_command + self.Curr_direction - 1) % 8
            if curr_command < 120:
                # check command
                dx, dy = self.Bias_dir[num_bias_dir]
                if x + dx >= map_.Size or x + dx < 0:
                    dx = -dx
                if y + dy >= map_.Size or y + dy < 0:
                    dy = -dy
                if map_.Field[x + dx][y + dy].is_bot_here():
                    self.Pointer_of_ai = (self.Pointer_of_ai + 3) % 256
                elif map_.Field[x + dx][y + dy].is_food_here():
                    self.Pointer_of_ai = (self.Pointer_of_ai + 4) % 256
                else:
                    self.Pointer_of_ai = (self.Pointer_of_ai + 5) % 256
            elif curr_command < 160:
                # rotate command
                self.Curr_direction = num_bias_dir
                self.Pointer_of_ai = (self.Pointer_of_ai + 1) % 256
            else:
                self.Pointer_of_ai = (self.Pointer_of_ai + curr_command) % 256
            curr_command = self.Ai.Gens[self.Pointer_of_ai]
            max_num_of_actions -= 1

        if 0 <= curr_command <= 39:
            action = "move"
        elif 40 <= curr_command <= 79:
            action = "attack"

        num_bias_dir = (curr_command + self.Curr_direction - 1) % 8
        dx, dy = self.Bias_dir[num_bias_dir]
        if x + dx >= map_.Size or x + dx < 0:
            dx = -dx
            self.Curr_direction = 3 if dx == 1 else 7
        if y + dy >= map_.Size or y + dy < 0:
            dy = -dy
            self.Curr_direction = 1 if dy == -1 else 5
        return dx, dy, action

    def print_info(self):
        """ Выводит информацию о состояние бота

        :return: Выводится всю внутренюю информацию о боте в терминал
        """
        print("Curr_direction = " + str(self.Curr_direction))
        print("Pointer_of_ai  = " + str(self.Pointer_of_ai))
        print("Life  = " + str(self.Life))
        print("Age  = " + str(self.Age))
        print("Death  = " + str(self.DeathTick))
        self.Dna.print_info()
        self.Ai.print_info()
        print("\n\n")

    def get_adaptation_value(self):
        """ Выдает значение адаптации

        :return:  Возвращаеь значение
        """
        value = self.Age * 1000
        value += 2000 if not self.DeathTick else self.DeathTick * 10
        value += self.Life
        return value


class AI:
    """ Искуственный интеллект бота
    """
    def __init__(self):
        self.Gens = array.array('B')
        self.set_ai()

    def set_ai(self):
        """ Инициализация бота

        :return: Бот со случайными 256 командами
        """
        for i in range(256):
            self.Gens.append(random.randint(0, 255))

    def print_info(self):
        """ Отладочная печать

        :return: Выводит всю информацию о ИИ в терминал
        """
        print("Gens AI:")
        for i in self.Gens:
            print(i, end=" ")
        print('\n')

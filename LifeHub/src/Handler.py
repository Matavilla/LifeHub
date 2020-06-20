"""
Данный модуль содержит обработчик вселенной игры. Он осуществляет все
необходимые действия каждого объекта игры за 1 тик. Также осуществляет
периодическую генерацию еды на карте.
"""

import random
import LifeHub.src.map as mp
import LifeHub.src.food as food
import LifeHub.src.bot as bot
import LifeHub.src.ga as ga

DEBUG = False


class Handler:
    """ Обработчик вселенной, который обрабатывает происходящее во
        вселенной за 1 тик.
    """
    def __init__(self, worldPar):
        self.World_par = worldPar
        self.Map = None
        self.BotCoordinates = [[], [], []]
        self.BotPopulation = [[], [], []]
        self.Tick = 1
        self.Period = 0

    def create_map(self):
        """ Функция, создающая игровое поле.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 50, 9, 9, 9, 50, 50, 50)
>>> world_par.update(100, 10, 50, 9, 9, 9, 2, 2, 2)
>>> world_par.WorldSize = 4
>>> hr = Handler(world_par)
>>> hr.create_map()
>>> for line in hr.Map.Field:
...     for el in line:
...             el.Biom in range(1, 4)
...
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
        """
        self.Map = mp.Map(self.World_par.WorldSize)
        self.Map.generate()

    def spawn_start_food(self):
        """ Функция, генерирущая начальное количество еды.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 5, 9, 9, 9, 21, 21, 21)
>>> world_par.WorldSize = 100
>>> hr = Handler(world_par)
>>> hr.create_map()
>>> hr.spawn_start_food()
>>> count1 = 0
>>> count2 = 0
>>> count3 = 0
>>> for line in hr.Map.Field:
...     for el in line:
...             if el.Biom == 1 and el.is_food_here():
...                  count1 += 1
...             elif el.Biom == 2 and el.is_food_here():
...                  count2 += 1
...             elif el.Biom == 3 and el.is_food_here():
...                  count3 += 1
...
...
>>> count1
5
>>> count2
5
>>> count3
5
        """
        count = self.World_par.AmountOfFood
        self.spawn_food(1, count, False)

        count = self.World_par.AmountOfFood
        self.spawn_food(2, count, False)

        count = self.World_par.AmountOfFood
        self.spawn_food(3, count, False)

    def create_world(self):
        """ Функция создания вселенной.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 5, 9, 9, 9, 21, 22, 23)
>>> world_par.WorldSize = 100
>>> hr = Handler(world_par)
>>> hr.create_world()
>>> count1 = 0
>>> count2 = 0
>>> count3 = 0
>>> for line in hr.Map.Field:
...     for el in line:
...             if el.Biom == 1 and el.is_bot_here():
...                  count1 += 1
...             elif el.Biom == 2 and el.is_bot_here():
...                  count2 += 1
...             elif el.Biom == 3 and el.is_bot_here():
...                  count3 += 1
...
...
>>> count1
21
>>> count2
22
>>> count3
23
        """
        self.create_map()

        self.spawn_start_food()

        count = self.World_par.NumBots1
        self.spawn_bots(1, count)

        count = self.World_par.NumBots2
        self.spawn_bots(2, count)

        count = self.World_par.NumBots3
        self.spawn_bots(3, count)

    def spawn_food(self, biom, count, respawn=True):
        """ Функция, генерирующая еду.

        :param biom: Номер биома.
        :param count: Количество генерируемой еды.
        :param respawn: флаг повторной генерации еды в 1 точке.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 5, 9, 9, 9, 21, 21, 21)
>>> world_par.WorldSize = 100
>>> hr = Handler(world_par)
>>> hr.create_map()
>>> hr.spawn_food(1, 10)
>>> count1 = 0
>>> count2 = 0
>>> count3 = 0
>>> for line in hr.Map.Field:
...     for el in line:
...             if el.Biom == 1 and el.is_food_here():
...                  count1 += 1
...             elif el.Biom == 2 and el.is_food_here():
...                  count2 += 1
...             elif el.Biom == 3 and el.is_food_here():
...                  count3 += 1
...
...
>>> count1
10
>>> count2
0
>>> count3
0
        """
        while count:
            x, y = random.choice(self.Map.Biom_coord[biom - 1])
            while self.Map.Field[x][y].is_bot_here()\
                    and (respawn or self.Map.Field[x][y].is_food_here()):
                x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_food(food.Food(biom))
            count -= 1

    def spawn_bots(self, biom, count):
        """ Функция, создающая стартовую популяцию ботов.

        :param biom: Номер боима.
        :param count: Количество ботов.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 5, 9, 9, 9, 21, 21, 21)
>>> world_par.WorldSize = 100
>>> hr = Handler(world_par)
>>> hr.create_map()
>>> hr.spawn_bots(1, 10)
>>> count1 = 0
>>> count2 = 0
>>> count3 = 0
>>> for line in hr.Map.Field:
...     for el in line:
...             if el.Biom == 1 and el.is_bot_here():
...                  count1 += 1
...             elif el.Biom == 2 and el.is_bot_here():
...                  count2 += 1
...             elif el.Biom == 3 and el.is_bot_here():
...                  count3 += 1
...
...
>>> count1
10
>>> count2
0
>>> count3
0
        """
        if len(self.BotPopulation[biom - 1]) != count:
            count -= len(self.BotPopulation[biom - 1])
            while count:
                self.BotPopulation[biom - 1].append(bot.Bot(biom))
                count -= 1
        for i in range(len(self.BotPopulation[biom - 1])):
            x, y = random.choice(self.Map.Biom_coord[biom - 1])
            while self.Map.Field[x][y].is_bot_here()\
                    or self.Map.Field[x][y].is_food_here():
                x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_bot(self.BotPopulation[biom - 1][i])
            self.BotCoordinates[biom - 1].append((x, y))

    def actions_of_bots(self):
        for j in range(3):
            for i, (x, y) in enumerate(self.BotCoordinates[j]):
                self.actions_of_bot(j, i, x, y)

    def actions_of_bot(self, j, i, x, y):
        """ Функция, задающая действие бота.

        :param j,i: Номер бота.
        :param x,y: Координата бота.
        """
        self.Map.Field[x][y].Bot_ref.Life -= 1
        self.Map.Field[x][y].Bot_ref.TimeSpeed -= 1
        bot = self.Map.Field[x][y].Bot_ref
        biom = self.Map.Field[x][y].Biom

        if biom == 1:
            damage = 1 - bot.Dna.get("weather_resistance_1") / 255
        elif biom == 2:
            damage = 1 - bot.Dna.get("weather_resistance_2") / 255
        elif biom == 3:
            damage = 1 - bot.Dna.get("weather_resistance_3") / 255

        self.Map.Field[x][y].Bot_ref.Life -= damage
        speed = bot.Dna.get("speed") // 52

        if bot.Life < 0:
            self.BotCoordinates[j].pop(i)
            bot.Life = 0
            bot.DeathTick = self.Tick
            self.Map.Field[x][y].Bot_ref = None
            return
        if bot.TimeSpeed > 0:
            return
        self.Map.Field[x][y].Bot_ref.TimeSpeed = 5 - speed

        dx, dy, action = self.Map.Field[x][y].Bot_ref.\
            get_dir_and_action(x, y, self.Map)

        if (dx != 0 or dy != 0) and action:
            self.action(i, j, x, y, dx, dy, action)

    def action(self, i, j, x, y, dx, dy, action):
        """ Функция, осуществляющая действие бота.

       :param j,i: Номер бота.
       :param x,y: Координаты бота
       :param dx,dy: Смещение бота.
       :param action: Действие бота.

>>> from LifeHub.GUI.MainMenu import WorldParameters
>>> world_par = WorldParameters()
>>> world_par.update(100, 10, 1, 9, 9, 9, 1, 1, 1)
>>> world_par.WorldSize = 100
>>> hr = Handler(world_par)
>>> hr.create_map()
>>> hr.Map.Field[0][0].Bot_ref = bot.Bot(1)
>>> hr.Map.Field[2][2].Bot_ref = bot.Bot(1)
>>> hr.Map.Field[0][1].Bot_ref = bot.Bot(1)
>>> hr.BotCoordinates = {1: [(0, 0), (0, 0), (0, 0), (0, 0)]}
>>> hr.action(0, 1, 2, 2, -1, -1, "move")
>>> hr.Map.Field[1][1].Bot_ref is not None
True
>>> hr.Map.Field[2][2].Bot_ref is None
True
>>> hr.action(0, 1, 0, 0, 0, 1, "move")
>>> hr.Map.Field[0][0].Bot_ref is not None
True
>>> hr.Map.Field[0][1].Bot_ref is None
False
       """

        bot = self.Map.Field[x][y].Bot_ref
        cell = self.Map.Field[x + dx][y + dy]

        if self.Period < self.World_par.ChaosMoment and \
                self.Map.Field[x][y].Biom != \
                self.Map.Field[x + dx][y + dy].Biom:
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + random.randint(0, 5)) % len(bot.Ai)
            return

        if cell.is_bot_here():
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + random.randint(0, 5)) % len(bot.Ai)
            if False and action == "attack":
                agr = random.randint(1, 255)
                if agr <= bot.Dna.get("agression"):
                    armor = cell.Bot_ref.Dna.get("armor") / 255
                    self.Map.Field[x + dx][y + dy].Bot_ref.Life -= \
                        (1 - armor) * \
                        bot.Dna.get("power")
                    if self.Map.Field[x + dx][y + dy].Bot_ref.Life <= 0:
                        self.Map.Field[x][y].Bot_ref.Life += \
                            bot.Dna.get("power")
        elif cell.is_food_here():
            f = cell.Food_ref
            bot.Pointer_of_ai = self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + random.randint(0, 5)) % len(bot.Ai)
            vulnerability = bot.Dna.get("poison_vulnerability") / 255
            damage_from_poison = f.Toxic_value * (1 - vulnerability)
            sens = random.randint(1, 255)
            if sens <= bot.Dna.get("sensity"):
                bot.Life += f.Food_value + f.Toxic_value
            else:
                bot.Life += f.Food_value - damage_from_poison

            self.Map.Field[x + dx][y + dy].Food_ref = None
            if action == "move":
                self.Map.Field[x + dx][y + dy].set_bot(bot)
                self.Map.Field[x][y].Bot_ref = None
                self.BotCoordinates[j][i] = (x + dx, y + dy)
        else:
            bot.Pointer_of_ai = self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + 5) % len(bot.Ai)
            if action == "move":
                self.Map.Field[x + dx][y + dy].set_bot(bot)
                self.Map.Field[x][y].Bot_ref = None
                self.BotCoordinates[j][i] = (x + dx, y + dy)

    def migration_bots(self):
        """ Функция миграции ботов.
        """
        self.BotPopulation[0].append(self.BotPopulation[1][0])
        self.BotPopulation[0].append(self.BotPopulation[2][0])
        self.BotPopulation[0][-1].Dna.Biom = 1
        self.BotPopulation[0][-2].Dna.Biom = 1

        self.BotPopulation[1].append(self.BotPopulation[0][0])
        self.BotPopulation[1].append(self.BotPopulation[2][0])
        self.BotPopulation[1][-1].Dna.Biom = 2
        self.BotPopulation[1][-2].Dna.Biom = 2

        self.BotPopulation[2].append(self.BotPopulation[0][0])
        self.BotPopulation[2].append(self.BotPopulation[1][0])
        self.BotPopulation[2][-1].Dna.Biom = 3
        self.BotPopulation[2][-2].Dna.Biom = 3

    def get_full_population(self):
        """ Функция, которая дополняет популяции до полных.
        """
        i = len(self.BotPopulation[0])
        count = i
        while i < self.World_par.NumBots1:
            self.BotPopulation[0].append(ga.Selection.get_child(
                ga.Selection.get_parent(self.BotPopulation[0][:count]),
                ga.Selection.get_parent(self.BotPopulation[0][:count]),
                1))
            i = len(self.BotPopulation[0])

        i = len(self.BotPopulation[1])
        count = i
        while i < self.World_par.NumBots2:
            self.BotPopulation[1].append(ga.Selection.get_child(
                ga.Selection.get_parent(self.BotPopulation[1][:count]),
                ga.Selection.get_parent(self.BotPopulation[1][:count]),
                2))
            i = len(self.BotPopulation[1])

        i = len(self.BotPopulation[2])
        count = i
        while i < self.World_par.NumBots3:
            self.BotPopulation[2].append(ga.Selection.get_child(
                ga.Selection.get_parent(self.BotPopulation[2][:count]),
                ga.Selection.get_parent(self.BotPopulation[2][:count]),
                3))
            i = len(self.BotPopulation[2])

    def selection_after_chaos(self):
        """ Функция селекции, после завершения периодов отбора.
        """
        i, j = len(self.BotPopulation[0]), len(self.BotPopulation[1])
        k = len(self.BotPopulation[2])

        self.get_full_population()

        while i < len(self.BotPopulation[0]):
            x, y = random.choice(self.Map.Biom_coord[0])
            while self.Map.Field[x][y].is_bot_here()\
                    or self.Map.Field[x][y].is_food_here():
                x, y = random.choice(self.Map.Biom_coord[0])
            self.Map.Field[x][y].set_bot(self.BotPopulation[0][i])
            self.BotCoordinates[0].append((x, y))

        while j < len(self.BotPopulation[1]):
            x, y = random.choice(self.Map.Biom_coord[1])
            while self.Map.Field[x][y].is_bot_here()\
                    or self.Map.Field[x][y].is_food_here():
                x, y = random.choice(self.Map.Biom_coord[1])
            self.Map.Field[x][y].set_bot(self.BotPopulation[1][j])
            self.BotCoordinates[1].append((x, y))

        while k < len(self.BotPopulation[2]):
            x, y = random.choice(self.Map.Biom_coord[2])
            while self.Map.Field[x][y].is_bot_here()\
                    or self.Map.Field[x][y].is_food_here():
                x, y = random.choice(self.Map.Biom_coord[2])
            self.Map.Field[x][y].set_bot(self.BotPopulation[2][k])
            self.BotCoordinates[2].append((x, y))

    def selection_before_chaos(self):
        """ Функция, осуществляющая селекцию во время периода отбора.
        """
        def sort_adaptation(bot):
            return bot.get_adaptation_value()

        self.BotPopulation[0].sort(key=sort_adaptation)
        self.BotPopulation[1].sort(key=sort_adaptation)
        self.BotPopulation[2].sort(key=sort_adaptation)

        COUNT_PARENTS = 10
        del self.BotPopulation[0][COUNT_PARENTS:]
        del self.BotPopulation[1][COUNT_PARENTS:]
        del self.BotPopulation[2][COUNT_PARENTS:]

        migration_enable = (self.Period % 10) == 0
        if migration_enable:
            self.migration_bots()

        if DEBUG:
            print("=" * 20)
            self.print_in_log()
            print("=" * 20)

        self.get_full_population()

        for j in range(3):
            for i, bot in enumerate(self.BotPopulation[j]): # noqa : F402
                if migration_enable and i > COUNT_PARENTS + 2:
                    break
                elif not migration_enable and i > COUNT_PARENTS:
                    break
                bot.Age += 1
                bot.Life = 600
                bot.DeathTick = 0
                bot.Point_of_ai = 0

    def print_in_log(self):
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")

        for j in range(3):
            for bot in self.BotPopulation[j]: # noqa : F402
                bot.print_info()

        print(f"Ticks = {self.Tick}")

    def RunOnTick(self):
        """Функция обработки происходящего во вселенной за 1 тик.
        """
        if True:  # and self.Period < self.World_par.ChaosMoment:
            countBots = len(self.BotCoordinates[0])
            countBots += len(self.BotCoordinates[1])
            countBots += len(self.BotCoordinates[2])

            sumBots = self.World_par.NumBots1
            sumBots += self.World_par.NumBots2
            sumBots += self.World_par.NumBots3
            if countBots < 0.2 * sumBots or self.Tick == 1500:
                self.Period += 1
                self.Map.clear()
                self.BotCoordinates = [[], [], []]

                self.selection_before_chaos()

                self.spawn_bots(1, self.World_par.NumBots1)
                self.spawn_bots(2, self.World_par.NumBots2)
                self.spawn_bots(3, self.World_par.NumBots3)

                self.spawn_start_food()

                self.Tick = 0
        else:
            if self.Tick % 1 == 0:
                self.selection_after_chaos()

        if not self.Tick % self.World_par.T_1:
            count = 4
            self.spawn_food(1, count)

        if not self.Tick % self.World_par.T_2:
            count = 4
            self.spawn_food(2, count)

        if not self.Tick % self.World_par.T_3:
            count = 4
            self.spawn_food(3, count)

        self.actions_of_bots()

        self.Tick += 1

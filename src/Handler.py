import random
import src.map as mp
import src.food as food
import src.bot as bot
import src.ga as ga

DEBUG = True


class Handler:
    """ Обработчик вселенной.

    Выполняет все действия вселенной за один тик времени.

    Хранит игровое поле со всеми объектами

    """
    def __init__(self, worldPar):
        self.World_par = worldPar
        self.Map = None
        self.BotCoordinates = [[], [], []]
        self.BotPopulation = [[], [], []]
        self.Tick = 1
        self.Period = 0

    def create_map(self):
        """ Создает игровое поле

        :return: Сгенерированное игровое поле
        """
        self.Map = mp.Map(self.World_par.WorldSize)
        self.Map.generate()

    def spawn_start_food(self):
        """ Генерирует еду в начальный момент времени во всех биомах

        :return: Еда на сгенерированном поле в начальный момент времени
        """
        count = self.World_par.AmountOfFood
        self.spawn_food(1, count, False)

        count = self.World_par.AmountOfFood
        self.spawn_food(2, count, False)

        count = self.World_par.AmountOfFood
        self.spawn_food(3, count, False)

    def create_world(self):
        """ Объединяет ботов, игровое поле и еду для начала игры

        :return: Готовое игровое поле
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
        """ Генерирует еду в биоме

        :param biom: биом в котором генерируется еда
        :param count: количество еды в данном биоме
        :param respawn: может ли функция сработать несколько раз?
        :return: В каждом биоме генерируется еда

        """
        while count:
            x, y = random.choice(self.Map.Biom_coord[biom - 1])
            while self.Map.Field[x][y].is_bot_here()\
                    and (respawn or self.Map.Field[x][y].is_food_here()):
                x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_food(food.Food(biom))
            count -= 1

    def spawn_bots(self, biom, count):
        """ Генерирует ботов в биоме

        :param biom: биом в котором генерируется бот
        :param count: количество ботов в данном биоме
        :return: Боты сгенерируются в каждом биоме в определенном количестве
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
        """ Определеляет действия ботов

        :return: Дальнейшие действия ботов
        """
        for j in range(3):
            for i, (x, y) in enumerate(self.BotCoordinates[j]):
                self.actions_of_bot(j, i, x, y)

    def actions_of_bot(self, j, i, x, y):
        """ Определеяет действия каждого из ботов

        :param j: biom number - 1
        :type j: int

        :param i: index of bot position in auxiliaty list
        :type i: int

        :param x: x coordinate of bot
        :type x: int

        :param y: y coordinate of bot
        :type y: int

        :return:
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
        """ Perform an action of bot in corresponding with his AI.

       :param j: biom number - 1
       :type j: int

       :param i: index of bot position in auxiliaty list
       :type i: int

       :param x: x coordinate of bot
       :type x: int

       :param y: y coordinate of bot
       :type y: int

       :param dx: bias of bot in map in direction of x coordinate
       :type dx: int

       :param dy: bias of bot in map in direction of y coordinate
       :type dy: int

       :param action: move or attack
       :type action: str
       """

        bot = self.Map.Field[x][y].Bot_ref
        cell = self.Map.Field[x + dx][y + dy]

        if self.Period < self.World_par.ChaosMoment and \
                self.Map.Field[x][y].Biom != \
                self.Map.Field[x + dx][y + dy].Biom:
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + 2) % 256
            return

        if cell.is_bot_here():
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                (bot.Pointer_of_ai + 3) % 256
            if action == "attack":
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
                (bot.Pointer_of_ai + 4) % 256
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
                (bot.Pointer_of_ai + 5) % 256
            if action == "move":
                self.Map.Field[x + dx][y + dy].set_bot(bot)
                self.Map.Field[x][y].Bot_ref = None
                self.BotCoordinates[j][i] = (x + dx, y + dy)

    def migration_bots(self):
        """ Определяет перемещение ботов

        :return: Итоговая позиция ботов
        """
        self.BotPopulation[0].append(random.choice(self.BotPopulation[1]))
        self.BotPopulation[0].append(random.choice(self.BotPopulation[2]))
        self.BotPopulation[0][-1].Dna.Biom = 1
        self.BotPopulation[0][-2].Dna.Biom = 1

        self.BotPopulation[1].append(random.choice(self.BotPopulation[0]))
        self.BotPopulation[1].append(random.choice(self.BotPopulation[2]))
        self.BotPopulation[1][-1].Dna.Biom = 2
        self.BotPopulation[1][-2].Dna.Biom = 2

        self.BotPopulation[2].append(random.choice(self.BotPopulation[0]))
        self.BotPopulation[2].append(random.choice(self.BotPopulation[1]))
        self.BotPopulation[2][-1].Dna.Biom = 3
        self.BotPopulation[2][-2].Dna.Biom = 3

    def get_full_population(self):
        """ Получение полной популяции (Я хз как перевести)

        :return: (Я просто ХЗ ЧТО ПИСАТЬ ТУТ)
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
        """ Определяет происходящее после момента селекции

        :return: Новые виды клеток с новыми параметрами
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
        """ Определяет селекцию до пикового момента

        :return: Новые виды клеток с новыми параметрами
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
            self.print_in_log()

        self.get_full_population()

        for j in range(3):
            for i, bot in enumerate(self.BotPopulation[j]): # noqa : F402
                if migration_enable and i > COUNT_PARENTS + 2:
                    break
                elif not migration_enable and i > COUNT_PARENTS:
                    break
                bot.Age += 1
                bot.Life = 300
                bot.DeathTick = 0

    def print_in_log(self):
        """ Дебажная функция выводящая информацию о ботах

        :return: Логи с информацией
        """
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")

        for j in range(3):
            for bot in self.BotPopulation[j]: # noqa : F402
                bot.print_info()

        print(f"Ticks = {self.Tick}")

    def RunOnTick(self):
        """Готовит изображение для вывода

        :return: Новое изображение
        """
        if self.Period < self.World_par.ChaosMoment:
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
            count = 2
            self.spawn_food(1, count)

        if not self.Tick % self.World_par.T_2:
            count = 3
            self.spawn_food(2, count)

        if not self.Tick % self.World_par.T_3:
            count = 4
            self.spawn_food(3, count)

        self.actions_of_bots()

        self.Tick += 1

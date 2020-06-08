import random
import src.map as mp
import src.food as food
import src.bot as bot
import src.ga as ga

DEBUG = True

class Handler:
    def __init__(self, worldPar):
        self.World_par = worldPar
        self.Map = None
        self.BotCoordinates = [[], [], []]
        self.BotPopulation = [[], [], []]
        self.Tick = 1
        self.Period = 0

    def create_map(self):
        self.Map = mp.Map(self.World_par.WorldSize)
        self.Map.generate()

    def spawn_start_food()
        count = self.World_par.AmountOfFood
        self.spawn_food(1, count)

        count = self.World_par.AmountOfFood
        self.spawn_food(2, count)

        count = self.World_par.AmountOfFood
        self.spawn_food(3, count)

    def create_world(self):
        self.create_map()
        
        self.spawn_start_food()

        count = self.World_par.NumBots1
        self.spawn_bots(1, count)

        count = self.World_par.NumBots2
        self.spawn_bots(2, count)

        count = self.World_par.NumBots3
        self.spawn_bots(3, count)

    def spawn_food(self, biom, count):
        while count:
            x, y = random.choice(self.Map.Biom_coord[biom - 1])
            while self.Map.Field[x][y].is_bot_here():
                x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_food(food.Food(biom))
            count -= 1

    def spawn_bots(self, biom, count):
        if len(self.BotPopulation[biom - 1] != count):
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
        for j in range(2):
            for i, (x, y) in enumerate(self.BotCoordinates[j]):
                self.actions_of_bot(j, i, x, y)

    def actions_of_bot(self, j, i, x, y):
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
            self.action(i, x, y, dx, dy, action)

    def action(self, i, x, y, dx, dy, action):
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
        self.BotPopulation[0].append(random.choice(self.BotPopulation[1]))
        self.BotPopulation[0].append(random.choice(self.BotPopulation[2]))
        self.BotPopulation[0][-1].Dna.Biom, self.BotPopulation[0][-2].Dna.Biom = 1, 1
            
        self.BotPopulation[1].append(random.choice(self.BotPopulation[0]))
        self.BotPopulation[1].append(random.choice(self.BotPopulation[2]))
        self.BotPopulation[1][-1].Dna.Biom, self.BotPopulation[1][-2].Dna.Biom = 2, 2
        self.BotPopulation[1][-1].set_color()
        self.BotPopulation[1][-2].set_color()
            
        self.BotPopulation[2].append(random.choice(self.BotPopulation[0]))
        self.BotPopulation[2].append(random.choice(self.BotPopulation[1]))
        self.BotPopulation[2][-1].Dna.Biom, self.BotPopulation[2][-2].Dna.Biom = 3, 3
        self.BotPopulation[2][-1].set_color()
        self.BotPopulation[2][-2].set_color()
            

    def selection_after_chaos(self):


    def selection_before_chaos(self):
        sort(self.BotPopulation[0], key = lambda bot: return bot.get_adaptation_value())
        sort(self.BotPopulation[1], key = lambda bot: return bot.get_adaptation_value())
        sort(self.BotPopulation[2], key = lambda bot: return bot.get_adaptation_value())
        
        COUNT_PARENTS = 10
        del self.BotPopulationp[0][COUNT_PARENTS:]
        del self.BotPopulationp[1][COUNT_PARENTS:]
        del self.BotPopulationp[2][COUNT_PARENTS:]

        migration_enable = (self.Period % 10) == 0
        if migration_enable:
            self.migration_bots()

        if DEBUG:
            self.print_in_log()

        #selection

        for biomBots in self.BotPopulation:
            for i, bot in enumerate(biomBots):
                if migration_enable and i > COUNT_PARENTS + 2:
                    break
                elif not migration_enable and i > COUNT_PARENTS:
                    break
                bot.Age += 1
                bot.DeathTick = 0
        self.Tick = 0

    def print_in_log(self):
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")
        print(f"Number of bots = {len(self.BotCoordinates)}")

        for j in range(2):
            for i, (x, y) in enumerate(self.BotCoordinates[j]):
                print(f"Coordinates: x = {x}, y = {y}")
                self.Map.Field[x][y].Bot_ref.print_info()

        print(f"Ticks = {self.Tick}")

    def RunOnTick(self):
        '''Готовит изображение для вывода

        '''
        if self.Period < self.World_par.ChaosMoment:
            countBots = len(self.BotCoordinates[0]) + len(self.BotCoordinates[1]) + len(self.BotCoordinates[2])
            if countBots < 0.2 * (self.World_par.NumBots1 + self.World_par.NumBots2 + self.World_par.NumBots3) or self.Tick == 1500:
                self.Period += 1
                self.Map.clear()

                self.selection_before_chaos()

                self.spawn_bots(1, self.World_par.NumBots1)
                self.spawn_bots(2, self.World_par.NumBots2)
                self.spawn_bots(3, self.World_par.NumBots3)

                self.spawn_start_food()

                self.Tick = 0
        else:
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

import random
import src.map as map
import src.food as food
import src.bot as bot


class Handler:   
    def __init__(self, worldPar):
        self.World_par = worldPar
        self.Map = None
        self.BotCoordinates = []
        self.Tick = 1

    def create_map(self):
        self.Map = map.Map(self.World_par.WorldSize)
        self.Map.generate()

    def create_world(self):
        self.create_map()

        count = self.World_par.AmountOfFood
        self.spawn_food(1, count)

        count = self.World_par.AmountOfFood
        self.spawn_food(2, count)

        count = self.World_par.AmountOfFood
        self.spawn_food(3, count)

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
        while count:
            x, y = random.choice(self.Map.Biom_coord[biom-1])
            while self.Map.Field[x][y].is_bot_here()\
                    or self.Map.Field[x][y].is_food_here():
                x, y = random.choice(self.Map.Biom_coord[biom - 1])
            self.Map.Field[x][y].set_bot(bot.Bot(biom))
            self.BotCoordinates.append((x, y))
            count -= 1

    def actions_of_bots(self):
        for i, (x, y) in enumerate(self.BotCoordinates):
            # output all info
            print(f"Number of bots = {len(self.BotCoordinates)}")
            print(f"Coordinates: x = {x}, y = {y}")
            self.Map.Field[x][y].Bot_ref.print_info()

            self.actions_of_bot(i, x, y)

            print(f"Ticks = {self.Tick}")

    def actions_of_bot(self, i, x, y):
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
            self.BotCoordinates.pop(i)
            self.Map.Field[x][y].Bot_ref = None
            return
        if bot.TimeSpeed > 0:
            return
        self.Map.Field[x][y].Bot_ref.TimeSpeed = 5 - speed

        dx, dy, action = self.Map.Field[x][y].Bot_ref.get_dir_and_action()
        if x + dx >= self.Map.Size or x + dx < 0:
            dx = 0
        if y + dy >= self.Map.Size or y + dy < 0:
            dy = 0

        if (dx != 0 or dy != 0) and action:
            self.action(i, x, y, dx, dy, action)

    def action(self, i, x, y, dx, dy, action):
        bot = self.Map.Field[x][y].Bot_ref
        cell = self.Map.Field[x + dx][y + dy]

        if self.Tick < self.World_par.ChaosMoment and \
           self.Map.Field[x][y].Biom != self.Map.Field[x + dx][y + dy].Biom:
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = (bot.Pointer_of_ai + 
                                                          2) % 64
            return

        if cell.is_bot_here():
            self.Map.Field[x][y].Bot_ref.Pointer_of_ai = (bot.Pointer_of_ai + 
                                                          3) % 64
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
                                (bot.Pointer_of_ai + 4) % 64
            if action == "move":
                vulnerability = bot.Dna.get("poison_vulnerability") / 255
                damage_from_poison = f.Toxic_value * (1 - vulnerability)
                if f.Food_value < damage_from_poison:
                    sens = random.randint(1, 255)
                    if sens > bot.Dna.get("sensity"):
                        bot.Life -= damage_from_poison - f.Food_value
                        self.Map.Field[x + dx][y + dy].set_bot(bot)
                        self.Map.Field[x + dx][y + dy].Food_ref = None
                        self.Map.Field[x][y].Bot_ref = None
                        self.BotCoordinates[i] = (x + dx, y + dy)
                else:
                    bot.Life += f.Food_value - damage_from_poison
                    self.Map.Field[x + dx][y + dy].set_bot(bot)
                    self.Map.Field[x + dx][y + dy].Food_ref = None
                    self.Map.Field[x][y].Bot_ref = None
                    self.BotCoordinates[i] = (x + dx, y + dy)
        else:
            bot.Pointer_of_ai = self.Map.Field[x][y].Bot_ref.Pointer_of_ai = \
                                (bot.Pointer_of_ai + 5) % 64
            if action == "move":
                self.Map.Field[x + dx][y + dy].set_bot(bot)
                self.Map.Field[x][y].Bot_ref = None
                self.BotCoordinates[i] = (x + dx, y + dy)

    def RunOnTick(self):
        '''Готовит изображение для вывода'''
        if not self.Tick % self.World_par.T_1:
          count = 3
          self.spawn_food(1, count)

        if not self.Tick % self.World_par.T_2:
          count = 4
          self.spawn_food(2, count)

        if not self.Tick % self.World_par.T_3:
          count = 5
          self.spawn_food(3, count)

        self.actions_of_bots()

        self.Tick += 1

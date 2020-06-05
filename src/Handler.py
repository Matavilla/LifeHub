import random

import src.map as map
import src.food as food
import src.bot as bot


class Handler:   
	def __init__(self, worldPar):
		self.World_par = worldPar
		self.Map = None
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
			while self.Map.Field[x][y].is_bot_here() or self.Map.Field[x][y].is_food_here():
				x, y = random.choice(self.Map.Biom_coord[biom - 1])
			self.Map.Field[x][y].set_food(food.Food(biom))
			count -= 1

	def spawn_bots(self, biom, count):
		while count:
			x, y = random.choice(self.Map.Biom_coord[biom-1])
			while self.Map.Field[x][y].is_bot_here() or self.Map.Field[x][y].is_food_here():
				x, y = random.choice(self.Map.Biom_coord[biom - 1])
			self.Map.Field[x][y].set_bot(bot.Bot(biom))
			count -= 1

	def actions_of_bots(self):
		for y in range(self.Map.Size):
			for x in range(self.Map.Size):
				if self.Map.Field[x][y].is_bot_here() and \
				   not self.Map.Field[x][y].Bot_ref.WasChecked:
					self.random_move(x, y)

		for y in range(self.Map.Size):
			for x in range(self.Map.Size):
				if self.Map.Field[x][y].is_bot_here():
					self.Map.Field[x][y].Bot_ref.WasChecked = False

	def random_move(self, x, y):
		self.Map.Field[x][y].Bot_ref.TimeSpeed -= 1
		bot = self.Map.Field[x][y].Bot_ref
		speed = bot.Dna.get("speed")
		if bot.TimeSpeed > 0:
			return
		self.Map.Field[x][y].Bot_ref.TimeSpeed = 10 - (speed - 1)
		dx, dy = 0, 0
		direction = random.randint(1,8)
		if direction == 1:
			dx, dy = -1, 1
		elif direction == 2:
			dx, dy = 0, 1
		elif direction == 3:
			dx, dy = 1, 1
		elif direction == 4:
			dx, dy = 1, 0
		elif direction == 5:
			dx, dy = 1, -1
		elif direction == 6:
			dx, dy = 0, -1
		elif direction == 7:
			dx, dy = -1, -1
		elif direction == 8:
			dx, dy = -1, 0

		if x + dx >= self.Map.Size or x + dx < 0:
			dx = 0
		if y + dy >= self.Map.Size or y + dy < 0:
			dy = 0

		#cell = self.Map.Field[x + dx][y + dy]

		if self.Map.Field[x + dx][y + dy].Biom == bot.Dna.Biom and\
		   not self.Map.Field[x + dx][y + dy].is_bot_here() and\
		   not self.Map.Field[x + dx][y + dy].is_food_here():
			self.Map.Field[x][y].set_bot(self.Map.Field[x + dx][y + dy].Bot_ref)
			self.Map.Field[x + dx][y + dy].set_bot(bot)
			self.Map.Field[x + dx][y + dy].Bot_ref.WasChecked = True

	def RunOnTick(self):
		'''Готовит изображение для вывода'''
		# if not self.Tick % self.World_par.T_1:
		# 	count = 1
		# 	self.spawn_food(1, count)

		# if not self.Tick % self.World_par.T_2:
		# 	count = 2
		# 	self.spawn_food(2, count)

		# if not self.Tick % self.World_par.T_3:
		# 	count = 3
		# 	self.spawn_food(3, count)

		self.actions_of_bots()

		self.Tick += 1

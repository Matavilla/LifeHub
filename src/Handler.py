# <<<<<<< HEAD
# from random import randint
# import pygame
# from src.cell import Cell
# from src.bot import Bot

# class Handler:
# 	def __init__(self, worldPar):
# 		self.wPar = worldPar
# 		self.CellsPerRow = 0
# 		self.CellsPerColl = 0
# 		self.Map = []
# 		self.TmpMap = []
# 		#self.generate_objects()

# 	def generate_objects(self, wPar):
# 		''' Стартовая генерация объектов.

# 		'''
# 		self.wPar = wPar
# 		cell_size = wPar.CellSize
# 		self.CellsPerRow = wPar.Width // cell_size
# 		self.CellsPerColl = wPar.Height // cell_size
# 		for i in range(0, self.CellsPerColl):
# 			self.Map.append([])
# 			for j in range(0, self.CellsPerRow):
# 				self.Map[i].append(Cell(i * cell_size, j * cell_size, cell_size))
# 		# Добавление ботов для теста
# 		self.Map[20][40] = Bot(20 * cell_size, 50 * cell_size, \
# 								cell_size, 1, (255, 0, 0), 1, True)

# 		self.Map[50][40] = Bot(20 * cell_size, 50 * cell_size, \
# 								cell_size, 1, (255, 0, 0), 1, True)

# 		self.Map[35][55] = Bot(20 * cell_size, 50 * cell_size, \
# 								cell_size, 1, (255, 0, 0), 1, True)

# 		self.Map[35][20] = Bot(20 * cell_size, 50 * cell_size, \
# 								cell_size, 1, (255, 0, 0), 1, True)



# 	def random_move(self, x, y):
# 		bot = self.Map[x][y]
# 		cell_size = self.wPar.CellSize
# 		if bot.Speed == 0:
# 			return
# 		dx, dy = 0, 0
# 		vert = bot.Speed
# 		hor = bot.Speed
# 		direction = randint(1,8)
# 		if direction == 1:
# 			dx, dy = -hor, vert
# 		elif direction == 2:
# 			dx, dy = 0, vert
# 		elif direction == 3:
# 			dx, dy = hor, vert
# 		elif direction == 4:
# 			dx, dy = hor, 0
# 		elif direction == 5:
# 			dx, dy = hor, -vert
# 		elif direction == 6:
# 			dx, dy = 0, -vert
# 		elif direction == 7:
# 			dx, dy = -hor, -vert
# 		elif direction == 8:
# 			dx, dy = -hor, 0

# 		if x + dx >= self.CellsPerRow or x + dx < 0:
# 			dx = 0
# 		if y + dy >= self.CellsPerColl or y + dy < 0:
# 			dy = 0

# 		bot.Bounds = pygame.Rect((x + dx) * cell_size, (y + dy) * cell_size,\
# 								cell_size, cell_size)
# 		bot.X = (x + dx) * cell_size
# 		bot.Y = (y + dy) * cell_size
# 		self.Map[x + dx][y + dy] = bot
# 		self.Map[x + dx][y + dy].WasChecked = True
		
# 		if dx != 0 or dy != 0:
# 			self.Map[x][y] = Cell(x * cell_size, y * cell_size, cell_size)

# 	def run_on_tick(self):
# 		'''Готовит изображение для вывода.

# 		'''
# 		#self.TmpMap = copy.deepcopy(self.Map)
# 		for i in range(0, self.CellsPerColl):
# 			for j in range(0, self.CellsPerRow):
# 				if self.Map[i][j].Alive and not self.Map[i][j].WasChecked:
# 					#self.Map[i][j].action_on_tick(self.Map, j, i)
# 					self.action_on_tick(i, j)
# 					self.Map[i][j].WasChecked = True

# 		for i in range(0, self.CellsPerColl):
# 			for j in range(0, self.CellsPerRow):
# 				self.Map[i][j].WasChecked = False

# 		#self.Map = self.TmpMap
# 		return self.Map

# 	def action_on_tick(self, x, y):
# 		cell_size = self.wPar.CellSize
# 		if self.Map[x][y].Life > 0:
# 			#self.check_around(x, y)
# 			self.random_move(x, y)
# 		else:
# 			self.Map[x][y] = Cell(x * cell_size, y * cell_size, cell_size)

#   #   def check_around(self, x, y):
#   #   	#bot = self.Map[x][y]
#   #   	agr = randint(1, 100)
# 		# for i in range(1, self.Sensity + 1):
# 		# 	if x - i < 0:
# 		# 		start_x = 0
# 		# 	else:
# 		# 		start_x = x - i

# 		# 	if x + i >= self.CellsPerRow:
# 		# 		fin_x = self.CellsPerRow - 1
# 		# 	else 
# 		# 		fin_x = x + i

# 		# 	if y - i >= 0:
# 		# 		for j in range(start_x, fin_x + 1):
# 		# 			if self.Map[j][y-i].Alive:
# 		# 				if agr <= bot.Agression:
# 		# 					if i == 1:
# 		# 						self.Map[j][y-1].Life -= 50

# 		# 	if y - i < 0:
# 		# 		start_y = 0
# 		# 	else:
# 		# 		start_y = y - i
# 		# 	if y + i >= self.CellsPerColl:
# 		# 		fin_y = self.CellsPerColl - 1
# 		# 	else 
# 		# 		fin_y = y + i

# 		# 	for j in range(start_y, fin_y + 1):
# 		# 		for k in range(start_x, fin_x + 1):
# 		# 			if 




# =======
import src.map as map


class Handler:   
    def __init__(self, worldPar):
        self.wPar = worldPar
        self.Map = None

    def create_map(self):
        self.Map = map.Map(self.wPar.WorldSize)
        self.Map.generate()

    def create_world(self):
        self.create_map()
#+ bot and food
        

    def RunOnTick(self):
        '''Готовит изображение для вывода'''
#>>>>>>> master

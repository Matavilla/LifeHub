from random import randint
import pygame
from src.cell import Cell
from src.bot import Bot

class Handler:
	def __init__(self, worldPar):
		self.wPar = worldPar
		self.CellsPerRow = 0
		self.CellsPerColl = 0
		self.Map = []
		self.TmpMap = []
		#self.generate_objects()

	def generate_objects(self, wPar):
		''' Стартовая генерация объектов.

		'''
		self.wPar = wPar
		cell_size = wPar.CellSize
		self.CellsPerRow = wPar.Width // cell_size
		self.CellsPerColl = wPar.Height // cell_size
		for i in range(0, self.CellsPerColl):
			self.Map.append([])
			for j in range(0, self.CellsPerRow):
				self.Map[i].append(Cell(i * cell_size, j * cell_size, cell_size))
		# Добавление одного бота для теста
		self.Map[20][50] = Bot(20 * cell_size, 50 * cell_size, \
								cell_size, 1, (255, 0, 0), 1, True)

	def random_move(self, x, y):
		bot = self.Map[x][y]
		cell_size = self.wPar.CellSize
		if bot.Speed == 0:
			return
		dx, dy = 0, 0
		vert = bot.Speed
		hor = bot.Speed
		direction = randint(1,4)
		if direction == 1:
			dx, dy = -hor, 0
		elif direction == 2:
			dx, dy = 0, -vert
		elif direction == 3:
			dx, dy = hor, 0
		elif direction == 4:
			dx, dy = 0, vert

		bot.Bounds = pygame.Rect((x + dx) * cell_size, (y + dy) * cell_size,\
								cell_size, cell_size)
		bot.X = (x + dx) * cell_size
		bot.Y = (y + dy) * cell_size
		self.TmpMap[x+dx][y+dy] = bot
		
		self.TmpMap[x][y] = Cell(x * cell_size, y * cell_size, cell_size)

	def run_on_tick(self):
		'''Готовит изображение для вывода.

		'''
		self.TmpMap = self.Map
		for i in range(0, self.CellsPerColl):
			for j in range(0, self.CellsPerRow):
				if self.Map[i][j].Alive:
					self.random_move(i, j)

		self.Map = self.TmpMap
		return self.Map


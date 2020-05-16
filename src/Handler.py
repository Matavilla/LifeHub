from random import randint
import pygame
from src.cell import Cell
from src.bot import Bot

class Handler:
	def __init__(self, worldPar):
		self.wPar = worldPar
		self.Map = []
		self.TmpMap = []
		self.generate_objects()

	def generate_objects(self):
		''' Стартовая генерация объектов.

		'''
		for i in range(0, 200): # 200 - параметр из wPar: кол-во клеток
			self.Map.append([])
			for j in range(0, 200): # кол-во клеток по столбцу
				self.Map[i].append(Cell(i * 4, j * 4, 4)) # 4 - размер клетки (далее в wPar)
		# Добавление одного бота для теста
		self.Map[100][100] = Bot(400, 400, 4, 1, (255, 0, 0), 1, True)

	def random_move(self, x, y):
		bot = self.Map[x][y]
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

		bot.Bounds = pygame.Rect((x + dx) * 4, (y + dy) * 4,  4, 4)
		bot.X = (x + dx) * 4
		bot.Y = (y + dy) * 4
		self.TmpMap[x+dx][y+dy] = bot
		
		self.TmpMap[x][y] = Cell(x * 4, y * 4, 4)

	def run_on_tick(self):
		'''Готовит изображение для вывода.

		'''
		self.TmpMap = self.Map
		for i in range(0, 200):
			for j in range(0, 200):
				if self.Map[i][j].Alive:
					self.random_move(i, j)

		self.Map = self.TmpMap
		return self.Map


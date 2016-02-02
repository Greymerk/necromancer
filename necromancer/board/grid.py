import pygame

from cell import Cell
from pygame.color import THECOLORS
from necromancer.util import Vector2

class Grid(object):

	rows = 6
	cols = 11

	def __init__(self):
		self.cells = []
		for x in range(Grid.cols):
			for y in range(Grid.rows):
				vec = Vector2(x, y)
				rect = pygame.Rect((x * Cell.size, y * Cell.size), (Cell.size, Cell.size))
				self.cells.append(Cell(vec))

	def getCellFromPos(self, pos):
		for cell in self.cells:
			if cell.pos == pos:
				return cell

	def inBounds(self, vec):
		
		if vec[0] < 0:
			return False

		if vec[0] >= Grid.cols:
			return False

		if vec[1] < 0:
			return False
		
		if vec[1] >= Grid.rows:
			return False

		return True
		
	def __iter__(self):
		return iter(self.cells)

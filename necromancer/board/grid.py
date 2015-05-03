import pygame

from cell import Cell
from pygame.color import THECOLORS
from necromancer.util import Vector2

class Grid(object):

	rows = 6
	cols = 11

	def __init__(self, point):
		self.cells = []
		self.point = point
		for x in range(Grid.cols):
			for y in range(Grid.rows):
				vec = Vector2(x, y)
				p = (point[0] + x * Cell.size, point[1] + y * Cell.size)
				self.cells.append(Cell(vec, p))

	def draw(self, surface):
		for cell in self.cells:
			cell.draw(surface)

	def getCellFromPos(self, pos):
		for cell in self.cells:
			if cell.pos == pos:
				return cell

	def getCellFromPoint(self, point):
		for cell in self.cells:
			if cell.collidePoint(point):
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

import pygame
from pygame.color import THECOLORS

from necromancer.units import UnitManager
from necromancer.units import Unit
from necromancer.util import Vector2


class Gameboard(object):

	rows = 6
	cols = 11

	def __init__(self):
		self.units = UnitManager()
		self.hover = None

	def update(self):
		self.units.update()

	def getEntity(self, pos):
		for unit in self.units.units:
			if pos == unit.pos:
				return unit
				
	def getSelected(self):
		return self.units.getSelected()

	def inBounds(self, vec):
		
		if vec[0] < 0:
			return False

		if vec[0] >= Gameboard.cols:
			return False

		if vec[1] < 0:
			return False
		
		if vec[1] >= Gameboard.rows:
			return False

		return True
		
	def __iter__(self):
		board = []
		for x in range(11):
			for y in range(6):
				board.append((x, y))
		return iter(board)

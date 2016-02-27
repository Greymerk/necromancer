import pygame
from pygame.color import THECOLORS

from necromancer.units import UnitManager
from necromancer.units import Unit
from grid import Grid
from necromancer.util import Vector2


class Gameboard(object):

	def __init__(self):
		self.grid = Grid()
		self.units = UnitManager(self.grid)
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
		return self.grid.inBounds(vec)
		
	def __iter__(self):
		board = []
		for x in range(11):
			for y in range(6):
				board.append((x, y))
		return iter(board)

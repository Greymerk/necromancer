import pygame
from pygame.color import THECOLORS

from necromancer.units import UnitManager
from necromancer.units import Unit
from grid import Grid
from necromancer.util import Vector2


class Gameboard(object):

	def __init__(self, point):
		self.grid = Grid(point)
		self.point = point
		self.units = UnitManager(self.grid)

	def update(self):
		self.units.update()

	def draw(self, surface):
		self.grid.draw(surface)
		self.units.draw(surface)

	def getEntity(self, pos):
		for unit in self.units.units:
			if pos == unit.pos:
				return unit

	def getSelected(self):
		return self.units.getSelected()

	def inBounds(self, vec):
		return self.grid.inBounds(vec)

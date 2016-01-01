import pygame
from pygame.color import THECOLORS
from necromancer.board import Cell

class UnitManager(object):

	def __init__(self, grid):
		self.units = []
		self.grid = grid		
		self.font = pygame.font.Font(None,24)
		self.previouslySelected = None

	def add(self, unit):
		self.units.append(unit)

	def getSelected(self):

		if len(self.units) == 0:
			return None

		if self.previouslySelected is None:
			self.previouslySelected = self.units[:1][0]

		if self.previouslySelected.hasInitiative():
			return self.previouslySelected

		for unit in self.units:
			if unit.hasInitiative() and self.previouslySelected.owner is not unit.owner:
				self.previouslySelected = unit
				return unit

		for unit in self.units:
			if unit.hasInitiative():
				self.previouslySelected = unit
				return unit

	def draw(self, surface):
		
		for unit in self.units:
			if unit.isDead():
				self.units.remove(unit)

		for unit in self.units:
			unit.draw(surface)

		order = []
		for unit in self.units:
			if unit.hasInitiative():
				order.append(unit)

		u = self.getSelected()

		if u is None:
			return

		owner = u.owner

		p1 = 0
		p2 = 0

		num = 0

		for i, unit in enumerate(order):
			if unit.owner is owner:
				num = p1
				p1 += 1
			else:
				num = p2
				p2 += 1
			cell = self.grid.getCellFromPos(unit.pos)
			surf = surface.subsurface(cell.getRect())
			surf.blit(self.font.render(str(num), 1, THECOLORS["white"]), (5, 5))


	def update(self):

		for unit in self.units:
			unit.update()

		for unit in self.units:
			if unit.isDead():
				self.units.remove(unit)
			
		self.previouslySelected = None

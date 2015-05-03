import pygame
from pygame.color import THECOLORS
from necromancer.board import Cell

class UnitManager(object):

	def __init__(self, grid):
		self.units = []
		self.grid = grid		
		self.font = pygame.font.Font(None,24)

	def add(self, unit):
		self.units.append(unit)

	def getSelected(self):
		for unit in self.units:
			if unit.hasInitiative():
				return unit

	def draw(self, surface):
		
		sel = self.getSelected()
		if sel is not None:
			for cell in self.grid.cells:
				if sel.validMove(cell.pos):
					cell.draw(surface, THECOLORS["yellow"])

		for unit in self.units:
			unit.draw(surface)

		order = []
		for unit in self.units:
			if unit.hasInitiative():
				order.append(unit)

		for i in range(len(order)):
			unit = order[i]
			cell = self.grid.getCellFromPos(unit.pos)
			surf = surface.subsurface(cell.getRect())
			surf.blit(self.font.render(str(i), 1, THECOLORS["white"]), (0, 0))


	def update(self):

		for unit in self.units:
			unit.update()

		for unit in self.units:
			if unit.isDead():
				self.units.remove(unit)

		
				

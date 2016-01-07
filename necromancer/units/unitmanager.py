import pygame
from pygame.color import THECOLORS
from necromancer.board import Cell

class UnitManager(object):

	def __init__(self, grid):
		self.units = []
		self.grid = grid		
		self.font = pygame.font.Font(None,24)
		self.selected = None
		self.time = 0		

	def add(self, unit):
		self.units.append(unit)

	def getSelected(self):

		if len(self.units) == 0:
			return None

		if self.selected is not None and not self.selected.done:
			return self.selected

		self.selected = self.units[0]
		for unit in self.units:
			if unit.nextTurn < self.selected.nextTurn:
				self.selected = unit

		time = self.selected.nextTurn
		for unit in self.units:
			unit.nextTurn -= time

		self.time += time
		self.selected.nextTurn = 1.0 / float(self.selected.speed)
		self.selected.done = False
		return self.selected

	def draw(self, surface):

		font = pygame.font.Font(None,24)
		msg = "time: " + str(self.time)
		color = (255,255,255)
		surface.blit(font.render(msg, 1, color), (155,80))
				
		for unit in self.units:
			if unit.isDead():
				self.units.remove(unit)

		for unit in self.units:
			unit.draw(surface)


	def update(self):

		for unit in self.units:
			if unit.isDead():
				self.units.remove(unit)
		
	def __iter__(self):
		return iter(self.units)

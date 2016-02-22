import pygame
from copy import deepcopy
from pygame.color import THECOLORS

from necromancer.board import Cell

class UnitManager(object):

	def __init__(self, grid):
		self.units = []
		self.grid = grid		
		self.font = pygame.font.Font(None,24)
		self.selected = None
		self.time = 0
		self.prediction = []
		
	def add(self, unit):
		self.units.append(unit)

	def predict(self, turns):
		clones = []
		
		for unit in self.units:
			clone = unit.clone()
			clones.append(clone)
		
		prediction = []
		simTime = self.time
		
		for turn in range(turns):
			selected = clones[0]
			for clone in clones:
				if clone.nextTurn < selected.nextTurn:
					selected = clone
				
			time = selected.nextTurn
			for clone in clones:
				clone.nextTurn -= time
		
			simTime += time
			selected.nextTurn = 1.0 / float(selected.speed)
			prediction.append(selected)
		
		results = []
		for clone in prediction:
			results.append(clone.original)
						
		return results
		
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
				
		self.prediction = self.predict(5)
		print "prediction"
		for unit in self.prediction:
			print str(unit.pos) + ' id:' + str(id(unit)) 
		
	def __iter__(self):
		return iter(self.units)

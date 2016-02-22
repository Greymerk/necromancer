import pygame
from pygame.color import THECOLORS

from necromancer.units import Unit

class SpawnMinion(object):

	def __init__(self, player):
		self.player = player
		self.observers = []
		self.font = pygame.font.Font(None,24)
			
	def draw(self, surface):
		if self.player.ability is self:
			surface.fill(THECOLORS["red"])
		else: 
			surface.fill(THECOLORS["yellow"])
			
		pygame.draw.rect(surface, THECOLORS["black"], surface.get_rect(), 1)
		surface.blit(self.font.render("Spawn", 1, THECOLORS["gray"]), (3,3))
	
	def action(self, cell):
		if self.player.validSpawn(cell.pos):
			self.player.board.units.add(Unit(self.player.board, cell.pos, self.player))

	def notify(self, event):
		for observer in self.observers:
			observer.notify(self, event)

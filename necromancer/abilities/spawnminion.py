import pygame
from pygame.color import THECOLORS

class SpawnMinion(object):

	def __init__(self, player):
		self.player = player
		self.observers = []
			
	def draw(self, surface):
		if self.player.ability is self:
			surface.fill(THECOLORS["red"])
		else: 
			surface.fill(THECOLORS["yellow"])
			
		pygame.draw.rect(surface, THECOLORS["black"], surface.get_rect(), 1)
	
	def notify(self, event):
		for observer in self.observers:
			observer.notify(self, event)

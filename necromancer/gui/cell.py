import pygame

from pygame.color import THECOLORS

class Cell(object):

	size = 64

	def __init__(self, surface, pos):
		self.surface = surface
		self.pos = pos
		self.observers = []
	
	def update(self):
		pass

	def draw(self, color = THECOLORS["black"]):
		padding = 4
		pad = pygame.Rect((0 + padding, 0 + padding), (Cell.size - padding * 2, Cell.size - padding * 2))
		pygame.draw.rect(self.surface, color, pad)

	def highlight(self, color = THECOLORS["white"]):
		padding = 4
		pad = pygame.Rect((0 + padding, 0 + padding), (Cell.size - padding * 2, Cell.size - padding * 2))
		pygame.draw.rect(self.surface, color, pad, 4)

	def notify(self, event):
		for observer in self.observers:
			observer.notify(self, event)

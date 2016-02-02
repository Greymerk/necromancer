import pygame

from pygame.color import THECOLORS

class Cell(object):

	size = 64

	def __init__(self, pos):
		self.pos = pos
	
	def update(self):
		pass

	def draw(self, surface, color = THECOLORS["black"]):
		padding = 4
		pad = pygame.Rect((0 + padding, 0 + padding), (Cell.size - padding * 2, Cell.size - padding * 2))
		pygame.draw.rect(surface, color, pad)

	def highlight(self, surface, color = THECOLORS["black"]):
		padding = 4
		pad = pygame.Rect((0 + padding, 0 + padding), (Cell.size - padding * 2, Cell.size - padding * 2))
		pygame.draw.rect(surface, color, pad, 4)

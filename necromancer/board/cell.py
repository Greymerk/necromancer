import pygame

from pygame.color import THECOLORS

class Cell(object):

	size = 64

	def __init__(self, pos, point):
		self.pos = pos
		self.point = point
	
	def update(self):
		pass

	def draw(self, surface, color = THECOLORS["black"]):
		padding = 4
		pad = pygame.Rect((self.point[0] + padding, self.point[1] + padding), (Cell.size - padding, Cell.size - padding))
		pygame.draw.rect(surface, color, pad)

	def highlight(self, surface, color = THECOLORS["black"]):
		padding = 4
		pad = pygame.Rect((self.point[0] + padding, self.point[1] + padding), (Cell.size - padding, Cell.size - padding))
		pygame.draw.rect(surface, color, pad, 4)
		
		
	def getRect(self):
		return pygame.Rect((self.point[0], self.point[1]),(Cell.size, Cell.size))

	def collidePoint(self, point):
		bounds = pygame.Rect((self.point[0], self.point[1]),(Cell.size, Cell.size))
		return bounds.collidepoint(point)



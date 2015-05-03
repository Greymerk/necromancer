import pygame

class Boardview(object):
	
	def __init__(self):
		pass

	def draw(self, surface, board):
		
		for row in range(6):
			for col in range(11):
				origin = col * 64 + 2, row * 64 + 2
				tile = pygame.Rect(origin, (60, 60))
				pygame.draw.rect(surface, (0,0,0), tile)

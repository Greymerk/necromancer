import pygame


class ControlState(object):
	
	def __init__(self):
		self.update()

	def update(self):
		self.pressed = pygame.mouse.get_pressed()
		self.pos = pygame.mouse.get_pos()
		self.event = pygame.event.get()

	

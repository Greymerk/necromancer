import pygame

class UnitControl(object):
	
	def __init__(self, player):
		self.player = player
		
	def notify(self, entity, event):

		if(event.type == pygame.MOUSEMOTION):
			self.player.board.hover = entity.pos
			return

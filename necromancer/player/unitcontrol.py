import pygame

class UnitControl(object):
	
	def __init__(self, player):
		self.player = player
		
	def notify(self, entity, event):

		if(event.type == pygame.MOUSEMOTION):
			self.player.board.hover = entity
			return
	
		if not entity.owner is self.player:
			return
		if entity.pos == cell.pos:
			entity.passTurn()
		if not entity.hasMoved and entity.validMove(cell.pos):
			entity.move(cell.pos)
		if entity.validAttackTarget(cell.pos):
			entity.attack(cell.pos)
import pygame
from necromancer.units import Unit

class CellControl(object):
	
	def __init__(self, player):
		self.player = player
		
	def notify(self, cell, event):
	
		if not self.player.control:
			return
	
		if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			entity = self.player.board.getSelected()
			if entity.pos == cell.pos:
				entity.passTurn()
			if not entity.hasMoved and entity.validMove(cell.pos):
				entity.move(cell.pos)
			if entity.validAttackTarget(cell.pos):
				entity.attack(cell.pos)
				
		if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
			print str(cell.pos)
			if self.player.validSpawn(cell.pos):
				self.player.board.units.add(Unit(self.player.board, cell.pos, self.player))
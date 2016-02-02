import pygame
from pygame.color import THECOLORS
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell

class BoardView(object):
	
	def __init__(self, surface, pos, game):
		self.surface = surface
		self.pos = pos
		self.game = game
		self.board = game.gameboard

	def getElement(self, vec):
		v = Vector2(vec)
		v -= self.pos
		pos = (int(v[0] / Cell.size), int(v[1] / Cell.size))
		return self.board.grid.getCellFromPos(pos)
		
	def draw(self):
		for x in range(11):
			for y in range(6):
				cell = self.board.getCellFromPos((x, y))
				rect = pygame.Rect((Cell.size * x, Cell.size * y),(Cell.size, Cell.size))
				surf = self.surface.subsurface(rect)
				cell.draw(surf)
				unit = self.board.getEntity((x, y))
				if(self.game.player.validSpawn(cell.pos)):
					cell.highlight(surf, THECOLORS["purple"])
				if(unit is not None):
					unit.draw(surf)
				sel = self.board.getSelected()
				if sel is not None and sel.owner is self.game.player:
					if not sel.hasMoved and sel.validMove(cell.pos):
						cell.highlight(surf, THECOLORS["green"])
					if sel.validAttackTarget(cell.pos):
						cell.highlight(surf, THECOLORS["red"])
				

	def highlight(self, cell, color):
		rect = pygame.Rect((cell.pos[0] * Cell.size, cell.pos[1] * Cell.size),(Cell.size, Cell.size))
		surf = self.surface.subsurface(rect)
		cell.highlight(surf, color)
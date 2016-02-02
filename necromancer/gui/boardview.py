import pygame
from pygame.color import THECOLORS
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell

class BoardView(object):
	
	def __init__(self, surface, game):
		self.surface = surface
		self.game = game
		self.board = game.board

	def getElement(self, vec):
		pos = (int(vec[0] / 64), int(vec[1] / 64))
		return self.board.grid.getCellFromPos(pos)
		
	def draw(self):
		for x in range(11):
			for y in range(6):
				cell = self.board.getCellFromPos((x, y))
				rect = pygame.Rect((Cell.size * x, Cell.size * y),(Cell.size, Cell.size))
				surf = self.surface.subsurface(rect)
				cell.draw(surf)
				unit = self.board.getEntity((x, y))
				if(unit is not None):
					unit.draw(surf)
				selected = self.board.getSelected()
				if selected is not None:
					if selected.validMove(cell.pos):
						cell.highlight(surf, THECOLORS["green"])

	def highlight(self, cell, color):
		rect = pygame.Rect((cell.pos[0] * Cell.size, cell.pos[1] * Cell.size),(Cell.size, Cell.size))
		surf = self.surface.subsurface(rect)
		cell.highlight(surf, color)
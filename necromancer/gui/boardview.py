import pygame
from pygame.color import THECOLORS
from necromancer.util.vector import Vector2
from cell import Cell

class BoardView(object):
	
	def __init__(self, surface, pos, game):
		self.surface = surface
		self.pos = pos
		self.game = game
		self.board = game.gameboard
		self.cells = {}
		for x in range(11):
			for y in range(6):
				rect = pygame.Rect((Cell.size * x, Cell.size * y),(Cell.size, Cell.size))
				surf = self.surface.subsurface(rect)
				c = Cell(surf, (x, y))
				c.observers.append(self.game.player.cellcontrol)
				self.cells[(x, y)] = c

		
	def draw(self):
		sel = self.board.getSelected()
		for c in self.cells.values():
			c.draw()
			unit = self.board.getEntity(c.pos)
			if unit is not None:
				unit.draw(c.surface)
				if(self.game.player.validSpawn(Vector2(c.pos))):
					c.highlight(THECOLORS["purple"])


		if self.board.hover is not None:
			pos = (int(self.board.hover[0]), int(self.board.hover[1]))
			self.cells[pos].highlight(THECOLORS["yellow"])
			
		'''
		for x in range(11):
			for y in range(6):
				cell = self.board.getCellFromPos((x, y))
				
				
				cell.draw(surf)
				unit = self.board.getEntity((x, y))


				if(unit is not None):
					unit.draw(surf)
				sel = self.board.getSelected()
				if sel is not None and sel.owner is self.game.player:
					if not sel.hasMoved and sel.validMove(cell.pos):
						cell.highlight(surf, THECOLORS["green"])
					if sel.validAttackTarget(cell.pos):
						cell.highlight(surf, THECOLORS["red"])
		'''		

	def highlight(self, cell, color):
		rect = pygame.Rect((cell.pos[0] * Cell.size, cell.pos[1] * Cell.size),(Cell.size, Cell.size))
		surf = self.surface.subsurface(rect)
		cell.highlight(surf, color)
		
		
	def notify(self, vec, event):
		v = Vector2(vec)
		v -= self.pos
		pos = (int(v[0] / Cell.size), int(v[1] / Cell.size))
		self.cells[(pos)].notify(event)

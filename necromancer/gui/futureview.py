import pygame
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell
from pygame.color import THECOLORS

class FutureView(object):

	def __init__(self, pos, surface, game):
		self.surface = surface
		self.pos = pos
		self.game = game
		self.units = game.gameboard.units
		
	def notify(self, pos, event):
		v = Vector2(pos)
		v -= self.pos
		y = int(v[1] / Cell.size)
		if y in range(len(self.units.prediction)):
			self.units.prediction[y].notify(event)
		
	def draw(self):
		for i, unit in enumerate(self.units.prediction):
			if i > 6:
				return
			rect = pygame.Rect((0, Cell.size * i), (Cell.size, Cell.size))
			surf = self.surface.subsurface(rect)
			unit.draw(surf)

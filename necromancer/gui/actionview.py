import pygame
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell
from pygame.color import THECOLORS

class ActionView(object):

	def __init__(self, pos, surface, game):
		self.surface = surface
		self.pos = pos
		self.game = game
		self.abilities = self.game.player.abilities
		
	def getElement(self, vec):
		v = Vector2(vec)
		v -= self.pos
		x = int(v[0] / Cell.size)
		if x in range(len(self.abilities)):
			return self.abilities[x]
		
		
		
	def draw(self):
		for i, ability in enumerate(self.abilities):
			rect = pygame.Rect((Cell.size * i, 0), (Cell.size, Cell.size))
			surf = self.surface.subsurface(rect)
			ability.draw(surf)

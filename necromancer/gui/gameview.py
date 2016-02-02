import pygame
from pygame.color import THECOLORS
from boardview import BoardView
from necromancer.util.vector import Vector2

class Gameview(object):

	def __init__(self, surface, game):
	
		self.surface = surface
		self.pos = (150, 100)
		self.boardRect = pygame.Rect(self.pos, (64 * 11, 64 * 6))
		boardSurf = surface.subsurface(self.boardRect)
		self.boardView = BoardView(boardSurf, game)
		self.gameboard = game.gameboard
		self.player = game.player

	def getElement(self, vec):
		v2 = Vector2(vec)
		v2 -= self.pos
		return self.boardView.getElement(v2)
		
	def draw(self):
		self.surface.fill(THECOLORS["grey23"])
		self.boardView.draw()
		cell = self.getElement(pygame.mouse.get_pos())
		if(cell is not None):
			self.boardView.highlight(cell, THECOLORS["yellow"])
		#self.player.draw()
		pygame.display.flip()


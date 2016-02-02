import pygame
from pygame.color import THECOLORS
from boardview import BoardView
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell

class Gameview(object):

	def __init__(self, surface, game):
	
		self.game = game
		self.surface = surface
		timePos = (150, 50)
		timeRect = (timePos, (Cell.size * 11, 32))
		self.font = pygame.font.Font(None,24)
		self.timeSurf = self.surface.subsurface(timeRect)
		
		self.boardPos = (150, 100)
		self.boardRect = pygame.Rect(self.boardPos, (Cell.size * 11, Cell.size * 6))
		boardSurf = surface.subsurface(self.boardRect)
		self.boardView = BoardView(boardSurf, self.boardPos, game)
		self.gameboard = game.gameboard
		self.player = game.player

	def getElement(self, vec):
		return self.boardView.getElement(vec)
		
	def draw(self):
		self.surface.fill(THECOLORS["grey23"])
		msg = "Time: " + str(self.game.time)
		self.timeSurf.blit(self.font.render(msg, 1, THECOLORS["gray"]), (0,0))
		self.boardView.draw()
		cell = self.getElement(pygame.mouse.get_pos())
		if(cell is not None):
			self.boardView.highlight(cell, THECOLORS["yellow"])
		#self.player.draw()
		pygame.display.flip()


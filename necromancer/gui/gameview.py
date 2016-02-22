import pygame
from pygame.color import THECOLORS
from boardview import BoardView
from actionview import ActionView
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell

class Gameview(object):

	def __init__(self, surface, game):
	
		self.game = game
		self.surface = surface
		
		timePos = (150, Cell.size / 2)
		timeRect = (timePos, (Cell.size * 11, 32))
		self.timeSurf = self.surface.subsurface(timeRect)
		
		self.boardPos = (150, Cell.size)
		self.boardRect = pygame.Rect(self.boardPos, (Cell.size * 11, Cell.size * 6))
		boardSurf = surface.subsurface(self.boardRect)
		self.boardView = BoardView(boardSurf, self.boardPos, game)
		
		self.actionPos = (150, self.boardPos[1] + Cell.size * 6 + Cell.size / 2)
		self.actionRect = pygame.Rect(self.actionPos, (Cell.size * 11, Cell.size))
		actionSurf = surface.subsurface(self.actionRect);
		self.actionView = ActionView(self.actionPos, actionSurf, game)
		
		self.gameboard = game.gameboard
		self.player = game.player
		self.font = pygame.font.Font(None,24)

	def getElement(self, vec):
		
		if self.actionRect.collidepoint(vec):
			return self.actionView.getElement(vec)
	
		if self.boardRect.collidepoint(vec):
			return self.boardView.getElement(vec)
		
		return None
		
	def draw(self):
		self.surface.fill(THECOLORS["grey23"])
		msg = "Time: " + str(self.game.time)
		self.timeSurf.blit(self.font.render(msg, 1, THECOLORS["gray"]), (0,0))
		self.boardView.draw()
		self.actionView.draw()
		
		element = self.getElement(pygame.mouse.get_pos())
		try:
			self.boardView.highlight(element, THECOLORS["yellow"])
		except:
			pass
			
		pygame.display.flip()
		

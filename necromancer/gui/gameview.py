import pygame
from pygame.color import THECOLORS
from boardview import BoardView
from actionview import ActionView
from futureview import FutureView
from necromancer.util.vector import Vector2
from necromancer.board.cell import Cell

class Gameview(object):

	def __init__(self, surface, game):
	
		self.game = game
		self.surface = surface
		
		left = 100
		
		timePos = (left, Cell.size / 2)
		timeRect = (timePos, (Cell.size * 11, 32))
		self.timeSurf = self.surface.subsurface(timeRect)
		
		self.boardPos = (left, Cell.size)
		self.boardRect = pygame.Rect(self.boardPos, (Cell.size * 11, Cell.size * 6))
		boardSurf = surface.subsurface(self.boardRect)
		self.boardView = BoardView(boardSurf, self.boardPos, game)
		
		self.actionPos = (left, self.boardPos[1] + Cell.size * 6 + Cell.size / 2)
		self.actionRect = pygame.Rect(self.actionPos, (Cell.size * 11, Cell.size))
		actionSurf = surface.subsurface(self.actionRect);
		self.actionView = ActionView(self.actionPos, actionSurf, game)
		
		self.futurePos = (left + 12 * Cell.size, Cell.size)
		self.futureRect = pygame.Rect(self.futurePos, (Cell.size, Cell.size * 6))
		futureSurf = surface.subsurface(self.futureRect)
		self.futureView = FutureView(self.futurePos, futureSurf, game)
		
		self.gameboard = game.gameboard
		self.player = game.player
		self.font = pygame.font.Font(None,24)

	def notify(self, vec, event):
		
		if self.actionRect.collidepoint(vec):
			return self.actionView.notify(vec, event)
	
		if self.boardRect.collidepoint(vec):
			return self.boardView.notify(vec, event)
		
		if self.futureRect.collidepoint(vec):
			return self.futureView.notify(vec, event)
		
		return None
		
	def draw(self):
		self.surface.fill(THECOLORS["grey23"])
		msg = "Time: " + str(self.game.time)
		self.timeSurf.blit(self.font.render(msg, 1, THECOLORS["gray"]), (0,0))
		self.boardView.draw()
		self.actionView.draw()
		self.futureView.draw()
		
		pygame.display.flip()
		

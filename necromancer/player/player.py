import pygame
from pygame.locals import *
from pygame.color import THECOLORS

from necromancer.util import Color
from necromancer.units import Unit
from necromancer.util import Vector2

class Player(object):

	
	def __init__(self, board):
		self.color = THECOLORS["yellow"]
		self.quit = False
		self.board = board
		self.board.units.add(Unit(self.board, Vector2(0, 0), self))
		#self.board.units.add(Unit(self.board, Vector2(0, 1), self))
		#self.board.units.add(Unit(self.board, Vector2(0, 2), self))
		#self.board.units.add(Unit(self.board, Vector2(0, 3), self))
		#self.board.units.add(Unit(self.board, Vector2(0, 4), self))
		#self.board.units.add(Unit(self.board, Vector2(0, 5), self))

	def update(self):
		pass

	def draw(self, surface):
		cell = self.board.grid.getCellFromPoint(pygame.mouse.get_pos())
		if cell is not None:
			cell.draw(surface, Color.rainbow())

	def turn(self, game, unit):
		
		event = pygame.event.get()

		for e in event:
			if(e.type == QUIT):
				self.quit = True
			
			elif(e.type == KEYDOWN):
				if(e.key == K_p):
					self.screenshot()
			
			elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
			
				cell = self.board.grid.getCellFromPoint(pygame.mouse.get_pos())
				if cell is not None:
					if unit.validMove(cell.pos):
						unit.move(cell.pos)
	
		
			
			
			
			



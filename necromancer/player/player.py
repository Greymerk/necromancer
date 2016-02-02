import pygame
from pygame.locals import *
from pygame.color import THECOLORS

from necromancer.util import Color
from necromancer.units import Unit
from necromancer.util import Vector2

class Player(object):

	
	def __init__(self, board):
		self.color = THECOLORS["deepskyblue1"]
		self.quit = False
		self.board = board
		self.control = True
		self.board.units.add(Unit(self.board, Vector2(0, 0), self))
		self.board.units.add(Unit(self.board, Vector2(0, 1), self))
		self.board.units.add(Unit(self.board, Vector2(0, 2), self))
		self.board.units.add(Unit(self.board, Vector2(0, 3), self))
		speedy = Unit(self.board, Vector2(0, 4), self)
		speedy.speed = 3
		self.board.units.add(speedy)


	def update(self):
		pass

	def turn(self, game, unit):
		
		event = pygame.event.get()

		for e in event:
			if(e.type == QUIT):
				self.quit = True
			
			elif(e.type == KEYDOWN):
				if(e.key == K_p):
					self.screenshot()
			
			elif e.type == pygame.MOUSEBUTTONUP and e.button == 3:
				cell = game.getElement(pygame.mouse.get_pos())
				if cell is not None and self.validSpawn(cell.pos):
					self.board.units.add(Unit(self.board, cell.pos, self))

			elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
				cell = game.getElement(pygame.mouse.get_pos())
				if cell is not None:
					if unit.pos == cell.pos:
						unit.passTurn()
					if not unit.hasMoved and unit.validMove(cell.pos):
						unit.move(cell.pos)
					if unit.validAttackTarget(cell.pos):
						unit.attack(cell.pos)

	def validSpawn(self, pos):
		if pos[0] is not 0:
			return False
		
		if self.board.getEntity(pos) is not None:
			return False
			
		return True
	
	def hasLost(self):
		
		for unit in self.board.units:
			if unit.owner is self:
				return False
		
		return True

import pygame
from pygame.locals import *
from pygame.color import THECOLORS

from necromancer.abilities import SpawnMinion

from necromancer.util import Color
from necromancer.units import Unit
from necromancer.util import Vector2

from unitcontrol import UnitControl
from cellcontrol import CellControl
from abilitycontrol import AbilityControl

class Player(object):

	
	def __init__(self, board):
		
		self.abilities = []
		self.abilities.append(SpawnMinion(self))
		self.abilities.append(SpawnMinion(self))
		self.abilities.append(SpawnMinion(self))
		self.ability = self.abilities[0]
		self.abilitycontrol = AbilityControl(self)
		for ability in self.abilities:
			ability.observers.append(self.abilitycontrol)
		self.unitcontrol = UnitControl(self)
		board.units.unitcontrol = self.unitcontrol
		self.cellcontrol = CellControl(self)
		for cell in board:
			cell.observers.append(self.cellcontrol)
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

			if(e.type in [pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]):
				mpos = pygame.mouse.get_pos()
				game.view.notify(mpos, e)
				
	def validSpawn(self, pos):
		if pos[0] != 0:
			return False
		
		if self.board.getEntity(pos) is not None:
			return False
			
		return True
	
	def hasLost(self):
		
		for unit in self.board.units:
			if unit.owner is self:
				return False
		
		return True

import time

import pygame

from board import Gameboard
from gui import Gameview
from player import Player
from levels import Level

class Game(object):

	FPS = 30

	def __init__(self):
		
		pygame.init()
		self.size = (1024, 600)
		self.surface = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		
		self.gameboard = Gameboard()
		self.player = Player(self.gameboard)
		self.level = Level(self.gameboard)
		self.level.update(0, self.gameboard)
		self.player.screenshot = self.printscreen
		self.view = Gameview(self.surface, self)
		
		self.time = 0
		
		while not (self.player.quit or self.player.hasLost()):
			self.clock.tick(Game.FPS)
			unit = self.gameboard.units.getSelected()
			if unit is None:
				continue
			if(int(self.time) is not int(self.gameboard.units.time)):
				self.level.update(int(self.gameboard.units.time), self.gameboard)
				self.gameboard.update()
			self.time = self.gameboard.units.time
			unit.owner.turn(self, unit)
			self.view.draw()
			self.gameboard.update()
		
	def printscreen(self):
		date = time.gmtime()
		fileName =	"screenshot_" + \
			str(date[0]) + '-' + \
			str(date[1]) + '-' + \
			str(date[2]) + '-' + \
			str(date[3]-8) + '-' + \
			str(date[4]) + '-' + \
			str(date[5]) + \
			'.jpg'
		pygame.image.save(self.surface, fileName)
			
		

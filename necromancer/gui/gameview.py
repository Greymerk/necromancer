import pygame
from pygame.color import THECOLORS

class Gameview(object):

	def __init__(self, gameboard, player):
		self.gameboard = gameboard
		self.player = player

	def draw(self, surface):
		surface.fill(THECOLORS["grey23"])
		self.gameboard.draw(surface)
		self.player.draw(surface)
		pygame.display.flip()


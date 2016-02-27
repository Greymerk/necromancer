import pygame

from cell import Cell
from pygame.color import THECOLORS
from necromancer.util import Vector2

class Grid(object):

	rows = 6
	cols = 11

	def __init__(self):
		pass


	def inBounds(self, vec):
		
		if vec[0] < 0:
			return False

		if vec[0] >= Grid.cols:
			return False

		if vec[1] < 0:
			return False
		
		if vec[1] >= Grid.rows:
			return False

		return True
		

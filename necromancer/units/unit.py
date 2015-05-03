import pygame
from pygame.color import THECOLORS

from necromancer.util import Vector2
from necromancer.board import Cell


class Unit(object):

	maxInitiative = 1

	def __init__(self, board, pos, owner=None):
		self.pos = pos
		self.owner = owner
		self.color = THECOLORS["white"]
		self.colorSelected = THECOLORS["green"]
		self.initiative = 0
		self.hasMoved = False
		self.hitpoints = 1
		self.range = 1
		self.board = board

	def update(self):
		self.initiative -= 1
		self.hasMoved = False

	def draw(self, surface):
		cell = self.board.grid.getCellFromPos(self.pos)
		r = cell.getRect()
		color = self.colorSelected if self.board.getSelected() is self else self.owner.color
		pygame.draw.circle(surface, color, (cell.point[0] + Cell.size/2, cell.point[1] + Cell.size/2), Cell.size/4)

	def validMove(self, pos):

		if not self.board.inBounds(pos):
			return False

		if not self.board.getEntity(pos) is None:
			return False

		if self.pos.dist(pos) > self.range:
			return False

		xDiff = abs(self.pos[0] - pos[0]);
		yDiff = abs(self.pos[1] - pos[1]);
	
		if(xDiff != 0 and yDiff != 0):
			return False;

		return True
		
	def move(self, vec):
		if vec is not self.pos:
			self.pos = vec
		self.hasMoved = True
		self.initiative = Unit.maxInitiative

	def moveToward(self, vec):
		nearest = None

		for cell in self.board.grid.cells:
			if not self.validMove(cell.pos):
				continue

			if nearest == None:
				nearest = cell
				continue

			if vec.dist(cell.pos) < vec.dist(nearest.pos):
				nearest = cell

		if nearest is None:
			self.move(self.pos)
			return

		self.move(nearest.pos)

	def hasInitiative(self):
		return self.initiative == 0

	def isDead(self):
		return self.hitpoints <= 0

	def getNearestEnemy(self):
		nearest = None

		for unit in self.board.units.units:

			if unit.owner == self.owner:
				continue

			if nearest is None:
				nearest = unit
				continue

			if self.pos.dist(unit.pos) < self.pos.dist(nearest.pos):
				nearest = unit

		return nearest

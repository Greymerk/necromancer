import pygame
from pygame.color import THECOLORS
import random


from necromancer.util import Color
from necromancer.util import Vector2
from pygame.color import THECOLORS

class Unit(object):

	OUTLINE = 4
	UNIT_SIZE = 16
	
	def __init__(self, board, pos, owner=None):
		self.pos = pos
		self.owner = owner
		self.color = THECOLORS["white"]
		self.colorSelected = THECOLORS["green"]
		self.done = False
		self.hasMoved = False
		self.nextTurn = 0
		self.hitpoints = 1
		self.speed = 1
		self.range = 1
		self.board = board
		self.nextTurn = random.random() * (1.0 / float(self.speed))
		self.observers = []

	def draw(self, surface):
		color = self.owner.color
		if self.hitpoints == 0:
			color = THECOLORS["white"]
		if self.board.getSelected() is self and self.owner.control:
			pygame.draw.circle(surface, Color.rainbow(), (32, 32), Unit.UNIT_SIZE + Unit.OUTLINE)
		pygame.draw.circle(surface, self.owner.color, (32, 32), Unit.UNIT_SIZE)
		
		if self.board.hover is not None and self.board.hover == self.pos:
			self.highlight(surface, Color.rainbow())

	def highlight(self, surface, color = THECOLORS["white"]):
		padding = 4
		pad = pygame.Rect((0 + padding, 0 + padding), (64 - padding * 2, 64 - padding * 2))
		pygame.draw.rect(surface, color, pad, 4)
		
	def clone(self):
		p = Vector2(self.pos[0], self.pos[1])
		cpy = Unit(self.board, p, self.owner)
		cpy.speed = self.speed
		cpy.done = self.done
		cpy.hasMoved = self.hasMoved
		cpy.nextTurn = self.nextTurn
		cpy.original = self
		return cpy
		
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

	def validAttackTarget(self, pos):

		unit = self.board.getEntity(pos)

		if not self.board.inBounds(pos):
			return False

		if unit is None:
			return False

		if unit.owner is self.owner:
			return False

		if self.pos.dist(pos) > 1:
			return False
		
		xDiff = abs(self.pos[0] - pos[0]);
		yDiff = abs(self.pos[1] - pos[1]);
	
		if(xDiff != 0 and yDiff != 0):
			return False;

		return True		

	def getNearbyAttackTarget(self):
		for unit in self.board.units.units:
			if self.validAttackTarget(unit.pos):
				return unit

	def attack(self, pos):
		target = self.board.getEntity(pos)
		if target is None:
			return
		target.damage(1, self)
		self.passTurn()

	def damage(self, damage, attacker):
		self.hitpoints -= damage

	def passTurn(self):
		self.hasMoved = False
		self.done = True
	
	def move(self, vec):
		self.pos = Vector2(vec)
		self.hasMoved = True
		if self.getNearbyAttackTarget() is None:
			self.passTurn()

	def moveToward(self, vec):
		nearest = None

		for pos in self.board:
			if not self.validMove(pos):
				continue

			if nearest == None:
				nearest = pos
				continue

			if vec.dist(pos) < vec.dist(nearest):
				nearest = pos

		if nearest is None:
			self.move(self.pos)
			return

		self.move(nearest)

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

			if self.validAttackTarget(unit.pos):
				return unit

		return nearest
		
	def notify(self, event):
		for observer in self.observers:
			observer.notify(self, event)

from pygame.color import THECOLORS

from necromancer.util import Vector2
from necromancer.units import Unit
from random import Random

class Level(object):

	def __init__(self, board):
		self.rand = Random("wosk")
		self.spawns = {}
		self.control = True
		self.color = THECOLORS["red"]
		self.spawns[0] = 1
		self.spawns[1] = 3
		self.spawns[2] = 1
		self.spawns[3] = 2

	def turn(self, game, unit):
		enemy = unit.getNearestEnemy()
		if enemy is None:
			return
		if unit.validAttackTarget(enemy.pos):
			unit.attack(enemy.pos)
		if not unit.hasMoved:
			unit.moveToward(enemy.pos)
			
	def update(self, turn, board):
		if not self.spawns.has_key(turn):
			return
			
		toSpawn = self.spawns[turn]
		for i in xrange(toSpawn):
			board.units.add(Unit(board, self.getSpawnPoint(board), self))
			
	def getSpawnPoint(self, board):
		pos = Vector2(10, self.rand.randint(0, 5))
		while(board.getEntity(pos) is not None):
			pos = Vector2(10, self.rand.randint(0, 5))
		return pos
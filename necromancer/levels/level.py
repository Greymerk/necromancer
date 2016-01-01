from pygame.color import THECOLORS

from necromancer.util import Vector2
from necromancer.units import Unit

class Level(object):


	def __init__(self, board):
		self.spawns = {}
		self.color = THECOLORS["red"]
		self.add(0, (10, 0))
		self.add(0, (10, 1))
		self.add(1, (10, 2))
		self.add(1, (10, 3))
		self.add(2, (10, 4))
		self.add(2, (10, 5))

	def turn(self, game, unit):
		enemy = unit.getNearestEnemy()
		if enemy is None:
			return
		if unit.validAttackTarget(enemy.pos):
			unit.attack(enemy.pos)
		if not unit.hasMoved:
			unit.moveToward(enemy.pos)

	def add(self, turn, toSpawn):
		if not self.spawns.has_key(turn):
			self.spawns[turn] = []
			
		turn_spawns = self.spawns[turn]
		turn_spawns.append(toSpawn)
		
	def update(self, turn, board):
		if not self.spawns.has_key(turn):
			return
			
		toSpawn = self.spawns[turn]
		for unit in toSpawn:
			board.units.add(Unit(board, Vector2(unit[0], unit[1]), self))
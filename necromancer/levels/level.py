from pygame.color import THECOLORS

from necromancer.util import Vector2
from necromancer.units import Unit

class Level(object):

	def __init__(self, board):
		self.color = THECOLORS["red"]
		board.units.add(Unit(board, Vector2(10, 0), self))
		board.units.add(Unit(board, Vector2(10, 1), self))
		board.units.add(Unit(board, Vector2(10, 2), self))
		board.units.add(Unit(board, Vector2(10, 3), self))
		board.units.add(Unit(board, Vector2(10, 4), self))
		board.units.add(Unit(board, Vector2(10, 5), self))

	def turn(self, game, unit):
		enemy = unit.getNearestEnemy()
		if enemy is None:
			return
		if unit.validAttackTarget(enemy.pos):
			unit.attack(enemy.pos)
		if not unit.hasMoved:
			unit.moveToward(enemy.pos)

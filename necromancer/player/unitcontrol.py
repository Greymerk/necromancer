
class UnitControl(object):
	
	def __init__(self, player):
		self.player = player
		
	def notify(entity, event):

		if not entity.owner is player:
			return
		if entity.pos == cell.pos:
			entity.passTurn()
		if not entity.hasMoved and entity.validMove(cell.pos):
			entity.move(cell.pos)
		if entity.validAttackTarget(cell.pos):
			entity.attack(cell.pos)
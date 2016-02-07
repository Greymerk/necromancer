import pygame

class AbilityControl(object):
	
	def __init__(self, player):
		self.player = player
	
	def notify(self, ability, event):
		if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			if self.player.ability is not ability:
				self.player.ability = ability
			else:
				self.player.ability = None
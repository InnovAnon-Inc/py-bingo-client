import pygame

from scene.scene_base  import SceneBase
from scene.game_scene  import GameScene
from scene.lobby_scene import LobbyScene
from cache.text_cache  import create_text

class EndGameScene(SceneBase):
	def __init__(self, winners, losers):
		SceneBase.__init__(self)
		self.winners = winners
		self.losers  = losers
    
	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				# Move to the next scene when the user pressed Enter
				# TODO construct new instance ?
				self.SwitchToScene(LobbyScene())
        
	def Update(self):
		pass
    
	def Render(self, screen):
		# The game scene is just a blank blue screen
		screen.fill((255, 0, 255))
		#print("Render Draw Scene")
		font_preferences = ["Comic Sans MS"]

		text = create_text("Winners", font_preferences, 56, (0, 128, 0))
		screen.blit(text, (0, 0))
		height = text.get_height()

		for winner in self.winners:
			text = create_text(winner, font_preferences, 32, (0, 128, 0))
			screen.blit(text, (0, height))
			height = height + text.get_height()
		
		text = create_text("Losers", font_preferences, 56, (0, 128, 0))
		screen.blit(text, (200, 0))
		height = text.get_height()

		for loser in self.losers:
			text = create_text(loser, font_preferences, 32, (0, 128, 0))
			screen.blit(text, (200, height))
			height = height + text.get_height()

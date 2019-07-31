import pygame

from scene.scene_base import SceneBase
from scene.game_scene import GameScene
from cache.text_cache import create_text

class DrawScene(SceneBase):
    def __init__(self, draw, board, history):
        SceneBase.__init__(self)
        self.draw    = draw
        self.board   = board
        self.history = history

        self.start_ticks = pygame.time.get_ticks()
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
		# TODO construct new instance ?
                self.SwitchToScene(GameScene(self.board, self.history))
                return
        if (pygame.time.get_ticks() - self.start_ticks) / 1000 > 1: self.SwitchToScene(GameScene(self.board, self.history))
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((255, 255, 0))
        #print("Render Draw Scene")
        font_preferences = ["Comic Sans MS"]
        text = create_text(str(self.draw), font_preferences, 72, (0, 128, 0))
        screen.blit(text, (200 - text.get_width() // 2, 150 - text.get_height() // 2))

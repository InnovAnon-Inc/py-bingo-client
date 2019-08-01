import pygame

from scene.scene_base    import SceneBase
#from scene.lobby_scene   import LobbyScene
#from scene.waiting_scene import WaitingScene
from scene.input_scene   import InputScene

from cache.text_cache import create_text

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(InputScene())
        
        #for event in events:
        #   if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        #       # Move to the next scene when the user pressed Enter
        #       self.SwitchToScene(LobbyScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        #print("Render Title Scene")

        font_preferences = ["Comic Sans MS"]
        text = create_text("Py-Bingo", font_preferences, 72, (0, 128, 0))
        screen.blit(text, (200 - text.get_width() // 2, 0))
        height = text.get_height()

        text = create_text("Python Bingo implementation", font_preferences, 32, (0, 128, 0))
        screen.blit(text, (200 - text.get_width() // 2, height))
        height = height + text.get_height()

        text = create_text("Special thanks to R. Fellini", font_preferences, 32, (0, 128, 0))
        screen.blit(text, (200 - text.get_width() // 2, height))

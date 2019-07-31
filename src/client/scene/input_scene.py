import pygame
import pygame_textinput

from scene.scene_base    import SceneBase
#from scene.lobby_scene   import LobbyScene
from scene.waiting_scene import WaitingScene

class InputScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.textinput = pygame_textinput.TextInput()
    
    def ProcessInput(self, events, pressed_keys):
        if self.textinput.update(events):
            self.SwitchToScene(WaitingScene(self.textinput.get_text()))
        
        #for event in events:
        #   if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        #       # Move to the next scene when the user pressed Enter
        #       self.SwitchToScene(LobbyScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((0, 255, 255))
        #print("Render Title Scene")
        screen.blit(self.textinput.get_surface(), (10, 10))

import pygame

from scene.scene_base    import SceneBase
#from scene.lobby_scene   import LobbyScene

class WaitingScene(SceneBase):
    def __init__(self, name):
        SceneBase.__init__(self)
        self.name = name
    
    def ProcessInput(self, events, pressed_keys):
        pass
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 255))
        #print("Render Title Scene")

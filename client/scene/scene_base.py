from abc import ABCMeta
from abc import abstractmethod

class SceneBase(object, metaclass=ABCMeta):
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys): raise Exception("uh-oh, you didn't override this in the child class")

    def Update(self): raise Exception("uh-oh, you didn't override this in the child class")

    def Render(self, screen): raise Exception("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene): self.next = next_scene
    
    def Terminate(self): self.SwitchToScene(None)

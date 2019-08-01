from scene.scene_base import SceneBase
from cache.text_cache import create_text

class GameScene(SceneBase):
    def __init__(self, board, history):
        SceneBase.__init__(self)
        self.board   = board
        self.history = history
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 255, 0))
        #print("Render Game Scene")

        font_preferences = ["Comic Sans MS"]
        height = 0
        rows = self.board.split("\n")
        for line in rows:
            width = 0
            cells = line.split(" ")
            for n in cells:
                text = create_text(str(n), font_preferences, 36, (0, 128, 0))
                screen.blit(text, (width, height))
                #width = width + text.get_width()
                width = width + 400 // len(cells)
            #height = height + text.get_height()
            height = height + 300 // len(rows)

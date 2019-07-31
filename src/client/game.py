#! /usr/bin/python3

import pygame

from scene.title_scene   import TitleScene
from scene.waiting_scene import WaitingScene

def is_trying_to_quit(event):
	pressed_keys = pygame.key.get_pressed()
	alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
	x_button = event.type == pygame.QUIT
	altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
	escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
	return x_button or altF4 or escape

class Game(object):
	def __init__(self, width=400, height=300, starting_scene=TitleScene()):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		self.clock = pygame.time.Clock()

		self.active_scene = starting_scene

	def run_game(self, fps):
		while self.active_scene != None:
			self.tick()
			self.clock.tick(fps)

	def tick(self):
		pressed_keys = pygame.key.get_pressed()
        
		# Event filtering
		filtered_events = []
		for event in pygame.event.get():
			if is_trying_to_quit(event):
				self.active_scene.Terminate()
			else:
			    filtered_events.append(event)
        
		self.active_scene.ProcessInput(filtered_events, pressed_keys)
		self.active_scene.Update()
		self.active_scene.Render(self.screen)
	        
		self.active_scene = self.active_scene.next
        
		pygame.display.flip()
	def isPhase2(self): return isinstance(self.active_scene, WaitingScene)

if __name__ == "__main__":
	g = Game(400, 300, TitleScene())
	g.run_game(60.0)

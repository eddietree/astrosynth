import pygame
import math
import SceneManager
import Globals

black = (0,0,0)
white = (255,255,255)

class Core:
    """A simple example class"""
    scene_mngr = None

    def __init__(self):

    	#create the screen
		Globals.window = pygame.display.set_mode(Globals.screen_size) 

		self.scene_mngr = SceneManager.SceneManager()
		#TODO: add scene

    def update(self):
    	Globals.time += 1.0/60.0
        self.scene_mngr.update()

    def draw(self):
        
    	Globals.window.fill((black))
        self.scene_mngr.draw()
    	pygame.display.flip() 
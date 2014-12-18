import pygame
import math
import SceneManager

g_window = 0
g_time = 0

black = (0,0,0)
white = (255,255,255)
y = 0

class Core:
    """A simple example class"""
    time = 0.0
    scene_mngr = None

    def __init__(self):

    	#create the screen
		global g_window
		g_window = pygame.display.set_mode((640, 480)) 

		self.scene_mngr = SceneManager.SceneManager()
		#TODO: add scene

    def update(self):
        global g_time
    	g_time += 1.0/60.0
        self.scene_mngr.update()

    def draw(self):

    	g_window.fill((black))
    	global y
    	y = 50 + math.sin(g_time * 0.1) * 100
    	pygame.draw.line(g_window, (255, 255, 255), (200, y), (230, 50+y))

        self.scene_mngr.draw()

    	pygame.display.flip() 
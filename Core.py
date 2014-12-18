import pygame
import math
import Scene

g_window = 0

black = (0,0,0)
white = (255,255,255)
y = 0

class Core:
    """A simple example class"""
    _time = 0.0

    def __init__(self):

    	#create the screen
		global g_window
		g_window = pygame.display.set_mode((640, 480)) 

		scene = Scene.Scene()
		scene.update();

    def update(self):
    	self._time += 1.0/60.0

    def draw(self):

    	g_window.fill((black))
    	global y
    	y = 50 + math.sin(self._time * 0.1) * 100
    	pygame.draw.line(g_window, (255, 255, 255), (200, y), (230, 50+y))
    	pygame.display.flip() 
import sys
import pygame
import math
from Core import *

def start():

	pygame.init() 

	core = Core()
	Globals.core = core
	
	quit = False
	while not quit: 

	   core.update()
	   core.draw()

	   for event in pygame.event.get(): 
	      if event.type == pygame.QUIT: 
	        sys.exit(0) 

	      # resize
	      elif event.type==pygame.VIDEORESIZE:
	      	screen_size = event.dict['size']
	      	Globals.screen_size = screen_size
	      	core.initWindow()
	      	print "Changed screen size to: " + screen_size

	      elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
	      	quit = True

	      else:
	        pass
	        #print event 

start()
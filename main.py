import sys
import pygame
import math
from Core import *

g_core = 0

def start():

	pygame.init() 

	global g_core
	g_core = Core()
	
	quit = False
	while not quit: 

	   g_core.update()
	   g_core.draw()

	   for event in pygame.event.get(): 
	      if event.type == pygame.QUIT: 
	        sys.exit(0) 
	      elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
	      	quit = True

	      else:
	        pass
	        #print event 

start()
import sys
import pygame
import math
from Core import *

g_window = 0
g_core = 0

def init():

	pygame.init() 
	
	global g_core
	g_core = Core()
	
init()

while True: 

   g_core.update()
   g_core.draw()

   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      #else: 
          #print event 
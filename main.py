import sys
import pygame
import math

pygame.init() 

window = 0
black = (0,0,0)
white = (255,255,255)
y = 0
time = 0.0

def init():
	#create the screen
	global window
	window = pygame.display.set_mode((640, 480)) 

def draw():

	window.fill((black))

	global y

	y = 50 + math.sin(time) * 100

	#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
	pygame.draw.line(window, (255, 255, 255), (200, y), (230, 50+y))

	for xx in range(0, 12):	
  		for yy in range(0, 16):
			pygame.draw.ellipse(window, white, [math.cos(time+yy)*20.0 + xx * 60, 10 + 30 *yy , 50, 20] )

	#draw it to the screen
	pygame.display.flip() 


init()


#input handling (somewhat boilerplate code):
while True: 
   time += 1.0/60.0

   draw()
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      #else: 
          #print event 
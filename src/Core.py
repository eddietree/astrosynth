import pygame
import math
import SceneManager
import Globals

class Core:
    """A simple example class"""
    scene_mngr = None
    ticks = pygame.time.get_ticks()

    def __init__(self):

        self.initWindow()

        # window title
        title = "ASTRO.SYNTH"
        pygame.display.set_caption(title, title)

        # screen scene manager
        self.scene_mngr = SceneManager.SceneManager()

    def initWindow(self):
        
        #create the screen
        flags =  pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF  # pygame.FULLSCREEN
        Globals.window = pygame.display.set_mode(Globals.screen_size, flags )


    def update(self):

        # calc delta time
        curr_ticks = pygame.time.get_ticks()
        dt = (curr_ticks - self.ticks) / 1000.0
        self.ticks = curr_ticks

    	Globals.time += max(dt, 1.0/60.0)
        self.scene_mngr.update()

    def draw(self):
        
    	Globals.window.fill((Globals.BLACK))
        self.scene_mngr.draw()
    	pygame.display.flip() 

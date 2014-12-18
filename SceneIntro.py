import math
import Scene
import Item
import pygame
import Globals

class ItemCircle(Item.Item):

    def __init__(self):
        Item.Item.__init__(self)

    def draw(self):
        y = 50 + math.sin(Globals.time * 0.1) * 100
        pygame.draw.line(Globals.window, (255, 255, 255), (200, y), (230, 50+y))

class SceneIntro(Scene.Scene):
    """A simple scene class"""

    def __init__(self):
        Scene.Scene.__init__(self)

        # add visuals
        self.add( ItemCircle(), "circle" )

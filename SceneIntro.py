import math
import Scene
import Item
import pygame
import Globals

class ItemCircle(Item.Item):

    def __init__(self):
        Item.Item.__init__(self)

    def draw(self):
        screen_width = Globals.screen_size[0]
        screen_height = Globals.screen_size[1]
        screen_center_x = screen_width * 0.5
        screen_center_y = screen_height * 0.5

        min_dimen = min(screen_width,screen_height)

        rect_width_delta = min_dimen * 0.1

        for i in range(1, 5):
            rect_width = rect_width_delta * i
            pygame.draw.rect(Globals.window, Globals.WHITE, [screen_center_x - rect_width*0.5, screen_center_y - rect_width*0.5, rect_width, rect_width], 1)

        y = 50 + math.sin(Globals.time * 0.1) * 100
        pygame.draw.line(Globals.window, (255, 255, 255), (200, y), (230, 50+y))

class SceneIntro(Scene.Scene):
    """A simple scene class"""

    def __init__(self):
        Scene.Scene.__init__(self)

        # add visuals
        self.add( ItemCircle(), "circle" )

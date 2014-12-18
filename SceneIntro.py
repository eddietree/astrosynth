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

        line_thickness = 2
        num_rings = 6
        rect_width_delta = min_dimen * 0.09
        time = Globals.time * 2.0

        rect_width_max = num_rings * rect_width_delta

        for i in range(0, num_rings):
            rect_width = (rect_width_delta * i + time) % rect_width_max
            
            alpha = math.sin( math.pi * rect_width / rect_width_max )
            color = (255*alpha, 255*alpha, 255*alpha)

            pygame.draw.rect(Globals.window, color, [screen_center_x - rect_width*0.5, screen_center_y - rect_width*0.5, rect_width, rect_width], line_thickness)

class SceneIntro(Scene.Scene):
    """A simple scene class"""

    def __init__(self):
        Scene.Scene.__init__(self)

        # add visuals
        self.add( ItemCircle(), "circle" )

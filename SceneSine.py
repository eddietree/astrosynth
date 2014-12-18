import math
import Scene
import Item
import pygame
import Globals

class ItemSine(Item.Item):

    freq = 440.0

    def __init__(self):
        Item.Item.__init__(self)

    def draw(self):
        screen_width = Globals.screen_size[0]
        screen_height = Globals.screen_size[1]
        screen_center_x = screen_width * 0.5
        screen_center_y = screen_height * 0.5

        x_buffer_percent = 0.2
        num_segs = 32

        x_start = screen_width * x_buffer_percent
        x_end = screen_width - x_start
        line_width = x_end - x_start
        inv_num_segs = 1.0 / num_segs
        delta_x = line_width * inv_num_segs

        # draw sine
        for i in range(0, num_segs):
            lerp_val = i * inv_num_segs

            pos_x = x_start + delta_x * i
            sine_val = math.sin( lerp_val * 2.0 * math.pi + Globals.time*0.1 )
            pos_y = screen_center_y + sine_val * 100.0

            color = Globals.WHITE
            pygame.draw.rect(Globals.window, color, [pos_x, pos_y, 5, 5])
        
class SceneSine(Scene.Scene):
    """A simple scene class"""

    def __init__(self):
        Scene.Scene.__init__(self)

        # add visuals
        self.add( ItemSine(), "sine" )

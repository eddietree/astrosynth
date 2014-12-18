import math
import Scene
import Item
import pygame
import Globals

class ItemSine(Item.Item):

    freq = 2.0

    def __init__(self):
        Item.Item.__init__(self)

        self.num_segs = 32
        self.pts = []

        for i in range(0, self.num_segs):
            self.pts.append( (0,0) )


    def draw(self):
        screen_width = Globals.screen_size[0]
        screen_height = Globals.screen_size[1]
        screen_center_x = screen_width * 0.5
        screen_center_y = screen_height * 0.5
        min_dimen = min(screen_width,screen_height)

        x_buffer_percent = 0.2
        num_segs = self.num_segs
        inv_num_segs = 1.0 / num_segs

        x_start = screen_width * x_buffer_percent
        x_end = screen_width - x_start
        line_width = x_end - x_start
       
        delta_x = line_width * inv_num_segs
        delta_y = screen_height * 0.15

        color = Globals.WHITE

        # draw sine
        for i in range(0, num_segs):
            lerp_val = i * inv_num_segs

            pos_x = x_start + delta_x * i
            sine_val = math.sin( self.freq * lerp_val * 2.0 * math.pi + Globals.time*0.15 )
            pos_y = screen_center_y + sine_val * delta_y

            self.pts[i] = (pos_x, pos_y)

        
        pygame.draw.lines(Globals.window, color, False, self.pts, 2 )
        
        pt_0 = self.pts[0]
        pt_1 = self.pts[-1]
        rect_width = min_dimen * 0.03
        pygame.draw.rect(Globals.window, color, [pt_0[0] - rect_width*0.5, pt_0[1] - rect_width*0.5, rect_width, rect_width] )
        pygame.draw.rect(Globals.window, color, [pt_1[0] - rect_width*0.5, pt_1[1] - rect_width*0.5, rect_width, rect_width] )
        
class SceneSine(Scene.Scene):
    """A simple scene class"""

    def __init__(self):
        Scene.Scene.__init__(self)

        # add visuals
        self.add( ItemSine(), "sine" )

from manim import * 
import numpy as np
class wave(Scene):
    def construct(self):
        axis = Axes(x_range=[-10,10],y_range=[-2,2])
        graph = axis.plot(lambda x:np.sin(x)+np.cos(x/2),color = WHITE)
        
        w1 = axis.plot(lambda x:np.sin(x),color = RED),
        w2 = axis.plot(lambda x:np.cos(x/2)*0.3,color = BLUE)
        
        w = VGroup(w1, w2)
        
        self.add(graph,axis)
        self.play(ReplacementTransform(graph,w))
        self.wait(1)
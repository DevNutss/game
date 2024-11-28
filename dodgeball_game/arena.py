import pymunk

class Arena:

    def __init__(self, space, screen_width, screen_height):
        self.space = space
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.create_boundaries()

    #create delimitations of the arena
    def create_boundaries(self):
        walls=[
            ((50,50),(self.screen_width - 50, 50)), #top wall
            ((self.screen_width, 50),(self.screen_width-50,self.screen_height-50)), #right wall 
            ((self.screen_width-50,self.screen_height-50),(50,self.screen_height-50)), #bottom wall 
            ((50,self.screen_height-50),(50,50)), #left wall
        ]
        for wall in walls: 
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Segment(body, wall[0],wall[1],5)
            shape.elasticity = 1.0
            self.space.add(body, shape)


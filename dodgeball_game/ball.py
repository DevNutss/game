import pygame
import pymunk

class Ball:
    def __init__(self, x, y, velocity, color, space):
        self.body = pymunk.Body()
        self.body.position = x, y 
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.color = color
        space.add(self.body, self.shape)

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.body.positio.x), int(self.body.position.y)), 20)
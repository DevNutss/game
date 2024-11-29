import pygame
import pymunk
import math
import random

class Ball:
    def __init__(self, x, y, direction, color, speed=10, radius=10):
        self.body = pymunk.Body()
        self.body.position = x, y 
        self.x = x
        self.y = y
        self.direction = direction  # Angle in degrees
        self.color = color
        self.speed = speed
        self.radius = radius
        self.dx = math.cos(math.radians(self.direction)) * self.speed
        self.dy = math.sin(math.radians(self.direction)) * self.speed

    
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def handle_collision(self, arena_width, arena_height):
        # Rebound off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= arena_width:
            self.dx = -self.dx
            self.dx += random.uniform(-1, 1)  # Add random direction change
        if self.y - self.radius <= 0 or self.y + self.radius >= arena_height:
            self.dy = -self.dy
            self.dy += random.uniform(-1, 1)  # Add random direction change
import pygame
import pymunk
import math
import random

class Ball:
    def __init__(self, x, y, angle, color, speed=10):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.radius = 10
        self.speed = speed

        # Compute movement vector
        angle_rad = math.radians(angle)
        self.dx = math.cos(angle_rad) * speed
        self.dy = -math.sin(angle_rad) * speed  # Negative because screen Y increases downward

    
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def handle_collision(self, arena_width, arena_height):
        # Rebound off walls
        if self.x - self.radius < 0 or self.x + self.radius > arena_width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > arena_height:
            self.dy *= -1
        # if self.x - self.radius <= 0 or self.x + self.radius >= arena_width:
        #     self.dx = -self.dx
        #     self.dx += random.uniform(-1, 1)  # Add random direction change
        # if self.y - self.radius <= 0 or self.y + self.radius >= arena_height:
        #     self.dy = -self.dy
        #     self.dy += random.uniform(-1, 1)  # Add random direction change
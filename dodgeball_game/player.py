import pygame
import math
from ball import Ball
from constants import *

class Player:
    def __init__(self, x, y, color, controls, starting_angle=0):
        self.color = color
        self.controls = controls #keys => movement's player
        self.angle = starting_angle
        self.original_width = 40
        self.original_height = 100
        self.rect = pygame.Rect(0,0, self.original_width, self.original_height)
        self.rect.center = (x,y)
        # self.surface.fill((0,0,0)) #transparent background
        # pygame.draw.rect(self.surface, color, (0,0,100,200))
        # self.rect = self.surface.get_rect(center=(x,y))
        #self.balls = []

    
    def move(self, pressed_keys):
        if pressed_keys[self.controls['up']]:
            self.rect.move_ip(0,-7)
        if pressed_keys[self.controls['down']]:
            self.rect.move_ip(0,7)  
        

    def rotate(self, pressed_keys):
        if pressed_keys[self.controls['left']]:
            self.angle += 2
        if pressed_keys[self.controls['right']]:
            self.angle -= 2

    def get_rotated_vertices(self):
        cx, cy = self.rect.center
        w, h = self.rect.size
        angle_rad = math.radians(self.angle)

         # Define rectangle corners relative to the center
        corners = [
            (-w / 2, -h / 2),
            (w / 2, -h / 2),
            (w / 2, h / 2),
            (-w / 2, h / 2),
        ]

        # Rotate each corner
        rotated_corners = []
        for x, y in corners:
            rx = cx + x * math.cos(angle_rad) - y * math.sin(angle_rad)
            ry = cy + x * math.sin(angle_rad) + y * math.cos(angle_rad)
            rotated_corners.append((rx, ry))

        return rotated_corners
    
    def clamp_within_arena(self, arena_rect):
        rotated_corners = self.get_rotated_vertices()
        
        # Check each corner against the arena bounds
        for x, y in rotated_corners:
            if x < arena_rect.left:
                self.rect.move_ip(arena_rect.left - x, 0)
            elif x > arena_rect.right:
                self.rect.move_ip(arena_rect.right - x, 0)
            if y < arena_rect.top:
                self.rect.move_ip(0, arena_rect.top - y)
            elif y > arena_rect.bottom:
                self.rect.move_ip(0, arena_rect.bottom - y)

    def draw(self, screen): #display player on screen
        # Create a rotated surface for the paddle
        surface = pygame.Surface((self.original_width, self.original_height), pygame.SRCALPHA)
        pygame.draw.rect(surface, self.color, (0, 0, self.original_width, self.original_height))

        # Rotate and blit the paddle
        rotated_surface = pygame.transform.rotate(surface, self.angle)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)
        screen.blit(rotated_surface, rotated_rect)

       
    def shoot(self):
        # Ball spawns slightly in front of the player
        angle_rad = math.radians(self.angle)

          # Calculate the offset for the ball spawn position
        offset_x = math.cos(angle_rad) * (self.original_height // 2 + 10)  # Slightly beyond the player's edge
        offset_y = -math.sin(angle_rad) * (self.original_height // 2 + 10)  # Negative for upward direction
        ball_x = self.rect.centerx + offset_x
        ball_y = self.rect.centery + offset_y

        ball_color = self.color #use player's color for balls 
        return Ball(ball_x, ball_y, math.degrees(angle_rad), ball_color, self)
    
    
    def collides_with(self, ball):
        # Use the player's rectangle for collision
        player_rect = self.rect
        
        # Create a rectangle for the ball
        ball_rect = pygame.Rect(
            ball.x - ball.radius, 
            ball.y - ball.radius, 
            ball.radius * 2, 
            ball.radius * 2
        )
        
        return player_rect.colliderect(ball_rect) and ball.shooter != self #prevent self_collision

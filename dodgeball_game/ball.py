import pygame
import pymunk
import math
import random

class Ball:
    def __init__(self, x, y, angle, color,shooter, speed=10):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.radius = 10
        self.speed = speed
        self.shooter = shooter #which shooter shot the ball 

        # Compute movement vector
        angle_rad = math.radians(angle)
        self.dx = math.cos(angle_rad) * speed
        self.dy = -math.sin(angle_rad) * speed  # Negative because screen Y increases downward

    
    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Add collision logic with the shooter
        if self.shooter.collides_with(self):
            print(f"Ball rebounded on shooter {self.shooter.color}")
            self.dx = -self.dx
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def handle_collision(self, arena_width, arena_height):
        # Rebound off walls
        if self.x - self.radius < 0 or self.x + self.radius > arena_width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > arena_height:
            self.dy *= -1

    def rebound_on_player(self, player):
        # Check if the ball collides with the player's rectangle
        player_rect = player.rect
        ball_rect = pygame.Rect(
            self.x - self.radius, 
            self.y - self.radius, 
            self.radius * 2, 
            self.radius * 2
        )

        if player_rect.colliderect(ball_rect):
            # Reverse ball direction
            self.dx = -self.dx
            self.dy = -self.dy
    
    def rebound_on_player(self, player):
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

        if ball_rect.colliderect(player.rect):
        # Calculate which side of the player's rectangle the ball is colliding with
            overlap_left = abs(ball_rect.right - player.rect.left)
            overlap_right = abs(ball_rect.left - player.rect.right)
            overlap_top = abs(ball_rect.bottom - player.rect.top)
            overlap_bottom = abs(ball_rect.top - player.rect.bottom)

            # Find the minimum overlap to determine the collision side
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_top and self.dy > 0:  # Top collision
                self.dy = -abs(self.dy)
            elif min_overlap == overlap_bottom and self.dy < 0:  # Bottom collision
                self.dy = abs(self.dy)
            elif min_overlap == overlap_left and self.dx > 0:  # Left collision
                self.dx = -abs(self.dx)
            elif min_overlap == overlap_right and self.dx < 0:  # Right collision
                self.dx = abs(self.dx)
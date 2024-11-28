import pygame
import pymunk
from arena import Arena
from player import Player
from ball import Ball
from constants import *


class Game: 
    def __init__(self):
        pygame.init()
       
        self.screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
        #get dynamic screen dimensions
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.running = True

    
        #Initialize arena and players
        self.arena = Arena(self.space, self.screen_width, self.screen_height)
        self.player1 = Player(100, self.screen_height//2, BLUE, {
            'up': pygame.K_w, 
            'down': pygame.K_s, 
            'left': pygame.K_a, 
            'right': pygame.K_d
            })
        self.player2 = Player(self.screen_width-100, self.screen_height//2, RED, {
            'up': pygame.K_UP, 
            'down': pygame.K_DOWN, 
            'left': pygame.K_LEFT, 
            'right': pygame.K_RIGHT
            })
        self.balls = []

    def run(self):
        #main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        #handle inputs - events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running = False
            if event.type==pygame.VIDEORESIZE: #handle screen resizing
                self.screen_width, self.screen_height = event.w, event.h
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                self.arena = Arena(self.space, self.screen_width, self.screen_height) #update boundaries

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        arena_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        # Update player positions and rotations
        self.player1.move(pressed_keys)
        self.player1.rotate(pressed_keys)
        self.player1.clamp_within_arena(arena_rect)

        self.player2.move(pressed_keys)
        self.player2.rotate(pressed_keys)
        self.player2.clamp_within_arena(arena_rect)

         # Handle shooting
        if pressed_keys[pygame.K_RETURN]:  # Player 1 shoots
            ball = self.player1.shoot()
            if ball:
                self.balls.append(ball)

        if pressed_keys[pygame.K_SPACE]:  # Player 2 shoots
            ball = self.player2.shoot()
            if ball:
                self.balls.append(ball)

        # Update balls
        for ball in self.balls:
            if self.player1.collides_with(ball):
                print("Player 1 hit!")
                self.balls.remove(ball)
            elif self.player2.collides_with(ball):
                print("Player 2 hit!")
                self.balls.remove(ball)


        # Step the physics space
        self.space.step(1 / 60)


    def draw(self):
        self.screen.fill(GRAY)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        for ball in self.balls:
            ball.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)


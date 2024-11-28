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
        arena_rect = pygame.Rect(0,0, self.screen_width, self.screen_height) #arena boundaries
        self.player1.move(pressed_keys, arena_rect)
        self.player1.rotate(pressed_keys)
        self.player2.move(pressed_keys, arena_rect)
        self.player2.rotate(pressed_keys)
        self.space.step(1/FPS)

    def draw(self):
        self.screen.fill(GRAY)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        for ball in self.balls:
            ball.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)

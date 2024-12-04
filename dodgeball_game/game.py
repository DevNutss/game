import pygame
import pymunk
from arena import Arena
from player import Player
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
        self.player2 = Player(self.screen_width - 100, self.screen_height // 2, RED, {
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT
            }, starting_angle=180)  # Face left by default
        self.balls = []

    def run(self):
        self.main_menu() #show menu window 
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
            if event.type==pygame.KEYDOWN:
                # Handle continuous key presses for shooting
                if event.key==pygame.K_SPACE:  # Player 1 shoots
                    self.balls.append(self.player1.shoot())
                if event.key==pygame.K_RETURN:  # Player 2 shoots
                    self.balls.append(self.player2.shoot())

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


        # Update balls
        for ball in self.balls[:]:
            ball.move()
            ball.handle_collision(self.screen_width, self.screen_height)

            # Rebound on its owner's rectangle
            # if ball.shooter == self.player1:
            #     ball.rebound_on_player(self.player1)
            # elif ball.shooter == self.player2:
            #     ball.rebound_on_player(self.player2)
                
            # Check for collisions with players
            if self.player1.collides_with(ball) and ball.shooter != self.player1:
                print("Player 1 hit!")
                self.player1.lives -= 1
                self.balls.remove(ball)
                if self.player1.lives <= 0:
                    self.game_over("Player 1")

            elif self.player2.collides_with(ball) and ball.shooter != self.player2:
                print("Player 2 hit!")
                self.player2.lives -= 1
                self.balls.remove(ball)
                if self.player2.lives <= 0:
                    self.game_over("Player 2")

        # Step the physics space
        self.space.step(1 / 60)


    def draw(self):
        self.screen.fill(GRAY)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        # Display hearts
        self.player1.draw_hearts(self.screen, 20, 20)  # Top-left corner
        self.player2.draw_hearts(self.screen, self.screen_width - 120, 20)  # Top-right corner

        for ball in self.balls:
            ball.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)

    def game_over(self, losing_player):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render(f"{losing_player} Loses!", True, RED)
        restart_text = font.render("Press R to Restart", True, WHITE)

        while True:
            self.screen.fill(BLACK)
            self.screen.blit(game_over_text, (self.screen_width // 2 - 200, self.screen_height // 2 - 100))
            self.screen.blit(restart_text, (self.screen_width // 2 - 200, self.screen_height // 2 + 50))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart the game
                        self.__init__()  # Reinitialize the game
                        return

    def main_menu(self):
        font = pygame.font.Font(None, 74)
        start_text = font.render("Press S to Start", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)

        while True:
            self.screen.fill(BLACK)
            self.screen.blit(start_text, (self.screen_width // 2 - 200, self.screen_height // 2 - 100))
            self.screen.blit(quit_text, (self.screen_width // 2 - 200, self.screen_height // 2 + 50))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Start the game
                        return
                    if event.key == pygame.K_q:  # Quit the game
                        pygame.quit()
                        exit()


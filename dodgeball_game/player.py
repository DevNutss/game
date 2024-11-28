import pygame

class Player:
    def __init__(self, x, y, color, keys):
        self.color = color
        self.keys = keys #keys => movement's player
        self.surface = pygame.Surface((100,200))
        self.surface.fill((0,0,0)) #transparent background
        pygame.draw.rect(self.surface, color, (0,0,100,200))
        self.rect = self.surface.get_rect(center=(x,y))
        self.angle = 0
        self.balls = []

    
    def move(self, pressed_keys, arena_rect):
        if pressed_keys[self.keys['up']]:
            self.rect.move_ip(0,-7)
        if pressed_keys[self.keys['down']]:
            self.rect.move_ip(0,7)  
        
        self.rect.clamp_ip(arena_rect)

    def rotate(self, pressed_keys):
        if pressed_keys[self.keys['left']]:
            self.angle += 2
        if pressed_keys[self.keys['right']]:
            self.angle -= 2

    def draw(self, screen): #display player on screen
        rotated_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA) #create a transparent surface
        pygame.draw.rect(rotated_surface,self.color, (0,0, *self.rect.size)) #draw paddle
        rotated_surface = pygame.transform.rotate(rotated_surface, self.angle)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center) #adjust position
        screen.blit(rotated_surface, rotated_rect) #blit rotated screen
    
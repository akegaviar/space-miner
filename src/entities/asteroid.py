import pygame
import random
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, RED, ASTEROID_SPEED

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(WINDOW_HEIGHT - self.rect.height)
        self.speed_x = random.choice([-ASTEROID_SPEED, ASTEROID_SPEED])
        self.speed_y = random.choice([-ASTEROID_SPEED, ASTEROID_SPEED])
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off screen edges
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.speed_y *= -1 
import pygame
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
        
        # Keep player on screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
    
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
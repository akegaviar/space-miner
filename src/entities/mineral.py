import pygame
import random
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, GREEN

class Mineral(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(WINDOW_HEIGHT - self.rect.height) 
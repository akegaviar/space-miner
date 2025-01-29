import pygame
from src.entities.player import Player
from src.entities.mineral import Mineral
from src.entities.asteroid import Asteroid
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BLACK

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Space Miner")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.player = Player()
        self.minerals = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        
        # Spawn initial minerals and asteroids
        for _ in range(5):
            self.minerals.add(Mineral())
            self.asteroids.add(Asteroid())
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.player.update()
        self.minerals.update()
        self.asteroids.update()
        
        # Check collisions
        pygame.sprite.spritecollide(self.player, self.minerals, True)
        if pygame.sprite.spritecollide(self.player, self.asteroids, False):
            self.running = False
    
    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.minerals.draw(self.screen)
        self.asteroids.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit() 
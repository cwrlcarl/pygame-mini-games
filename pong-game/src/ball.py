import pygame
import random
from settings import WHITE

class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.color = WHITE
        self.rect = pygame.Rect(x, y, self.radius, self.radius)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-3, 3])
        self.has_bounced = False
        self.scored = False

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
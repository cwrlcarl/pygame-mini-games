import pygame
from settings import SCREEN_HEIGHT

class Paddle:
    def __init__(self, x, y, color):
        self.color = color
        self.width, self.height = 10, 80
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 10

    def update_paddle1(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if k[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def update_paddle2(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if k[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
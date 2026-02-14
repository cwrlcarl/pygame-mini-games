import pygame
from settings import load_assets, SCREEN_WIDTH, SCREEN_HEIGHT

class Base:
    def __init__(self):
        tile = load_assets()['sprites']['base']
        tile_width = tile.get_width()
        self.image = pygame.Surface((SCREEN_WIDTH * 2, tile_width))
        self.rect = self.image.get_rect()

        for x in range(0, SCREEN_WIDTH * 2, tile_width):
            self.image.blit(tile, (x, 0))

        self.x1 = 0
        self.x2 = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - 100
        self.rect.topleft = (0, self.y)
        self.speed = 3

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 + SCREEN_WIDTH < 0:
            self.x1 = SCREEN_WIDTH
        if self.x2 + SCREEN_WIDTH < 0:
            self.x2 = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))
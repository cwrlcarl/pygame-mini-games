import pygame
from settings import load_assets, SCREEN_WIDTH, SCREEN_HEIGHT

class Base:
    def __init__(self):
        tile = load_assets()['sprites']['base']
        self.tile_width = tile.get_width()
        tile_height = tile.get_height()
        total_width = self.tile_width * 3

        self.image = pygame.Surface((total_width, tile_height))
        self.rect = self.image.get_rect()
        for x in range(0, total_width, self.tile_width):
            self.image.blit(tile, (x, 0))

        self.x = 0.0
        self.y = SCREEN_HEIGHT - 100
        self.rect.topleft = (0, self.y)
        self.speed = 3

    def update(self):
        self.x -= self.speed
        if self.x <= -self.tile_width:
            self.x += self.tile_width

    def draw(self, screen):
        screen.blit(self.image, (int(self.x), self.y))


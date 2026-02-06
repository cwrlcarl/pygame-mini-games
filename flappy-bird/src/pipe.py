import random
from settings import load_assets

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(300, 550)
        self.image = load_assets()['sprites']['pipe']
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.gap_y
        self.color = (59, 212, 102)
        self.speed = 3

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
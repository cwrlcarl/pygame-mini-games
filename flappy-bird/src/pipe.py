import random
from settings import load_assets

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pipe_gap = 75
        self.color = (59, 212, 102)
        self.speed = 3

        self.top_pipe = load_assets()['sprites']['top_pipe']
        self.top_rect = self.top_pipe.get_rect()
        self.top_rect.bottomleft = (x, self.y - self.pipe_gap)

        self.bottom_pipe = load_assets()['sprites']['bottom_pipe']
        self.bottom_rect = self.bottom_pipe.get_rect()
        self.bottom_rect.topleft = (x, self.y + self.pipe_gap)

    def update(self):
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.top_pipe, self.top_rect)
        screen.blit(self.bottom_pipe, self.bottom_rect)
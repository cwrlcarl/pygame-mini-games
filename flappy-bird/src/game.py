import pygame
from bird import Bird
from pipe import Pipe
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.assets = load_assets()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird 🐤")

        self.clock = pygame.time.Clock()
        self.running = True

        self.bird = Bird()

        self.pipes = []
        self.pipe_gap = 250
        self.last_pipe_x = SCREEN_WIDTH
        self.spawn_pipe()

    def update(self):
        self.bird.update()

        for pipe in self.pipes:
            pipe.update()

        if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - self.pipe_gap:
            self.spawn_pipe()

        for pipe in self.pipes[:]:
            if pipe.rect.right < 0:
                self.pipes.remove(pipe)

    def spawn_pipe(self):
        pipe = Pipe(SCREEN_WIDTH)
        self.pipes.append(pipe)
        self.last_pipe_x += SCREEN_WIDTH + self.pipe_gap

    def draw(self):
        self.screen.blit(load_assets()['sprites']['background'].convert(), (0, 0))
        self.bird.draw(self.screen)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jump_bird()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.jump_bird()

            self.update()
            self.draw()

    def jump_bird(self):
        self.assets['audio']['wing'].play()
        self.bird.is_jumping = True
        self.bird.velocity = self.bird.jump_strength
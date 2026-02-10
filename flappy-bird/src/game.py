import pygame
import random
from base import Base
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
        self.pipe_gap_x = 200
        self.last_pipe_x = SCREEN_WIDTH
        self.spawn_pipe()
        self.base = Base()
        self.ground_level = self.base.y
        self.start = False
        self.score = 0
        self.game_over = False

    def spawn_pipe(self):
        pipe = Pipe(SCREEN_WIDTH + 50, random.randint(250, 400))
        self.pipes.append(pipe)
        self.last_pipe_x += SCREEN_WIDTH + self.pipe_gap_x

    def check_collisions(self):
        for pipe in self.pipes:
            if pipe.top_rect.colliderect(self.bird.rect) or \
                pipe.bottom_rect.colliderect(self.bird.rect):
                self.game_over = True

        if self.bird.rect.bottom >= self.ground_level:
            self.bird.rect.bottom = self.ground_level
            self.game_over = True

    def display_score(self):
        for pipe in self.pipes:
            if self.bird.rect.right > pipe.top_rect.right and not pipe.scored:
                load_assets()['audio']['point'].play()
                pipe.scored = True
                self.score += 1

    def update(self):
        if not self.game_over:
            self.bird.update()
            self.base.update()

            if self.start:
                for pipe in self.pipes:
                    pipe.update()
                if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - self.pipe_gap_x:
                    self.spawn_pipe()
                for pipe in self.pipes[:]:
                    if pipe.bottom_rect.right < 0:
                        self.pipes.remove(pipe)

            self.display_score()
            self.check_collisions()

    def draw_ui(self):
        if not self.start:
            message_width, message_height = load_assets()['sprites']['message'].get_size()
            x = (SCREEN_WIDTH - message_width) / 2
            y = SCREEN_HEIGHT / 2 - message_height + 50
            self.screen.blit(load_assets()['sprites']['message'],(x, y))

        score_text = score_font.render(f"{self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) / 2, 20))

    def draw_sprites(self):
        self.screen.blit(load_assets()['sprites']['background'].convert(), (0, 0))

        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.base.draw(self.screen)
        self.bird.draw(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.bird.bottom:
                        self.jump_bird()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.jump_bird()

            self.update()
            self.draw_sprites()
            self.draw_ui()
            pygame.display.update()

    def jump_bird(self):
        if not self.game_over:
            self.assets['audio']['wing'].play()
            self.start = True
            self.bird.is_jumping = True
            self.bird.velocity = self.bird.jump_strength
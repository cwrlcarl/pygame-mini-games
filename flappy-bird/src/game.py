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
        self.game_started = None
        self.game_over = None
        self._initialize_game_state()

    def _initialize_game_state(self):
        self.assets['audio']['swoosh'].play()
        self.bird = Bird()
        self.pipes = []
        self.pipe_gap_x = 200
        self.last_pipe_x = SCREEN_WIDTH
        self.spawn_pipe()
        self.base = Base()
        self.ground_level = self.base.y
        self.game_started = False
        self.game_over = False
        self.score = 0

    def reset(self):
        self._initialize_game_state()

    def spawn_pipe(self):
        pipe = Pipe(SCREEN_WIDTH + 50, random.randint(200, 400))
        self.pipes.append(pipe)
        self.last_pipe_x += SCREEN_WIDTH + self.pipe_gap_x

    def handle_game_over(self):
        self.assets['audio']['hit'].play()
        self.game_over = True

    def handle_pipe_collision(self):
        for pipe in self.pipes:
            if pipe.top_rect.colliderect(self.bird.rect) or \
                pipe.bottom_rect.colliderect(self.bird.rect):
                self.handle_game_over()

    def handle_ground_collision(self):
        if self.bird.rect.bottom >= self.ground_level:
            self.bird.rect.bottom = self.ground_level
            self.handle_game_over()

    def check_collisions(self):
        self.handle_pipe_collision()
        self.handle_ground_collision()

    def display_score(self):
        for pipe in self.pipes:
            if self.bird.rect.right > pipe.top_rect.right and not pipe.scored:
                self.assets['audio']['point'].play()
                self.score += 1
                pipe.scored = True

    def update_pipe(self):
        if self.game_started:
            for pipe in self.pipes:
                pipe.update()
            if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - self.pipe_gap_x:
                self.spawn_pipe()
            for pipe in self.pipes[:]:
                if pipe.bottom_rect.right < 0:
                    self.pipes.remove(pipe)

    def update(self):
        if not self.game_over:
            self.bird.update()
            self.base.update()
            self.update_pipe()
            self.display_score()
            self.check_collisions()

    def draw_message(self):
        if not self.game_started:
            width, height = self.assets['sprites']['message'].get_size()
            x = (SCREEN_WIDTH - width) / 2
            y = 120
            self.screen.blit(self.assets['sprites']['message'],(x, y))

    def draw_score(self):
        score = str(self.score)
        numbers = self.assets['sprites']['numbers']
        digit_width = numbers[0].get_width()
        total_width = len(score) * digit_width
        starting_x, y = (SCREEN_WIDTH - total_width) / 2, 30
        for i, digit in enumerate(score):
            number = numbers[int(digit)]
            x = starting_x + (i * digit_width)
            self.screen.blit(number, (x, y))

    def draw_game_over(self):
        if self.game_over:
            width, height = self.assets['sprites']['game_over'].get_size()
            x = (SCREEN_WIDTH - width) / 2
            y = (SCREEN_HEIGHT - height - 100) / 2
            self.screen.blit(self.assets['sprites']['game_over'], (x, y))

    def draw_ui(self):
        self.draw_message()
        self.draw_score()
        self.draw_game_over()

    def draw_sprites(self):
        self.screen.blit(self.assets['sprites']['background'].convert(), (0, 0))
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.base.draw(self.screen)
        self.bird.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.jump_bird()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump_bird()
                if event.key == pygame.K_r and self.game_over:
                    self.reset()
                if event.key == pygame.K_ESCAPE and self.game_over:
                    self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw_sprites()
            self.draw_ui()
            pygame.display.update()

    def jump_bird(self):
        if not self.game_over:
            self.assets['audio']['wing'].play()
            self.game_started = True
            self.bird.is_jumping = True
            self.bird.velocity = self.bird.jump_strength
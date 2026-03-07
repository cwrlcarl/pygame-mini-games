import pygame
from ball import Ball
from paddle import Paddle
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pong Game')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.ui_starting_y = 55
        self.start_time = None
        self.game_over = None
        self.ball = None
        self._initialize_game_state()

    def _initialize_game_state(self):
        self.ball = None
        self.ball_speed = 12
        self.paddle1 = Paddle(50, SCREEN_HEIGHT // 2, PLAYER_PADDLE_COLOR)
        self.paddle2 = Paddle(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2, ENEMY_PADDLE_COLOR)
        self.player_score = 0
        self.enemy_score = 0
        self.winning_score = 5
        self.start_time = pygame.time.get_ticks()
        self.game_over = False

    @staticmethod
    def get_center_pos(object_rect):
        return (SCREEN_WIDTH // 2 - object_rect.get_width()) // 2

    def display_score_text(self):
        player_score = TEXT_FONT.render(f'{self.player_score}', True, WHITE)
        self.screen.blit(player_score, (self.get_center_pos(player_score), self.ui_starting_y))
        enemy_score = TEXT_FONT.render(f'{self.enemy_score}', True, WHITE)
        self.screen.blit(enemy_score, (SCREEN_WIDTH // 2 + self.get_center_pos(enemy_score), self.ui_starting_y))

    def display_winner_text(self):
        if self.game_over:
            result1 = "Win" if self.player_score == self.winning_score else "Lose"
            result2 = "Win" if self.enemy_score == self.winning_score else "Lose"
            player_side = TEXT_FONT.render(f'{result1}', True, WHITE)
            self.screen.blit(player_side, (self.get_center_pos(player_side), self.ui_starting_y + 100))
            enemy_side = TEXT_FONT.render(f'{result2}', True, WHITE)
            self.screen.blit(enemy_side, (SCREEN_WIDTH // 2 + self.get_center_pos(enemy_side), self.ui_starting_y + 100))

    def draw_line(self):
        width, height, gap_size, x = 5, 15, 15, SCREEN_WIDTH // 2
        for dash in range(17):
            y = self.ui_starting_y + dash * (height + gap_size)
            pygame.draw.rect(self.screen, DIVIDER_COLOR,
                             pygame.Rect(x, y, width, height))

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.display_score_text()
        self.display_winner_text()
        self.draw_line()
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        if self.ball is not None:
            self.ball.draw(self.screen)
        pygame.display.flip()

    def _spawn_ball(self):
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def respawn_ball(self):
        if self.start_time is None:
            self.start_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        if elapsed_time > 600:
            SPAWN_SFX.play()
            self._spawn_ball()
            self.start_time = None

    def check_overlap(self, paddle):
        overlap = self.ball.rect.centery - paddle.rect.centery
        half_height = paddle.rect.height // 2
        if abs(overlap) < 5:
            self.ball.dy = 3 if self.ball.dy > 0 else -3
        else:
            self.ball.dy = max(-8, min(8, overlap / half_height * 8))

    def handle_score(self):
        if self.ball is not None:
            if self.ball.rect.right < 0:
                if not self.ball.scored:
                    SCORE_SFX.play()
                    self.ball.scored = True
                    self.enemy_score += 1
                    self.ball = None
                if not self.game_over:
                    self.respawn_ball()
            elif self.ball.rect.left > SCREEN_WIDTH:
                if not self.ball.scored:
                    SCORE_SFX.play()
                    self.ball.scored = True
                    self.player_score += 1
                    self.ball = None
                if not self.game_over:
                    self.respawn_ball()

        if (self.player_score == self.winning_score or
                self.enemy_score == self.winning_score) and not self.game_over:
            GAME_OVER_SFX.play()
            self.game_over = True

    def handle_collisions(self):
        if self.ball is not None:
            if self.ball.rect.colliderect(self.paddle1.rect):
                PADDLE_HIT.play()
                self.ball.has_bounced = True
                self.check_overlap(self.paddle1)
                self.ball.dx *= -1
            elif self.ball.rect.colliderect(self.paddle2.rect):
                PADDLE_HIT.play()
                self.ball.has_bounced = True
                self.check_overlap(self.paddle2)
                self.ball.dx *= -1

            if (self.ball.rect.top < 0 or
                    self.ball.rect.bottom > SCREEN_HEIGHT):
                WALL_HIT.play()
                self.ball.dy *= -1

            if self.ball.has_bounced:
                self.ball.dx = self.ball.dx / abs(self.ball.dx) * self.ball_speed

    def update(self):
        if self.ball is None:
            self.respawn_ball()

        if not self.game_over:
            self.paddle1.update_paddle1()
            if self.ball is not None:
                self.paddle2.update_ai(self.ball)
                self.ball.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.game_over:
                    self.running = False
                if event.key == pygame.K_r and self.game_over:
                    self._initialize_game_state()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.handle_score()
            self.handle_collisions()
            self.update()
            self.events()
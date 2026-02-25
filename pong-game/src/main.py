import pygame
import random

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
SCORE_FONT = pygame.font.SysFont('Monocraft', 50)
WHITE = (235, 237, 245)
BG_COLOR = (22, 23, 26)
DIVIDER_COLOR = (64, 64, 64)
PLAYER_PADDLE_COLOR = (51, 61, 196)
ENEMY_PADDLE_COLOR = (196, 51, 63)

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
        self._initialize_game_state()

    def _initialize_game_state(self):
        self.ball = None
        self.ball_speed = 10
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
        player_score = SCORE_FONT.render(f'{self.player_score}', True, WHITE)
        self.screen.blit(player_score, (self.get_center_pos(player_score), self.ui_starting_y))
        enemy_score = SCORE_FONT.render(f'{self.enemy_score}', True, WHITE)
        self.screen.blit(enemy_score, (SCREEN_WIDTH // 2 + self.get_center_pos(enemy_score), self.ui_starting_y))

    def display_winner_text(self):
        if self.game_over:
            result1 = "Win" if self.player_score == self.winning_score else "Lose"
            result2 = "Win" if self.enemy_score == self.winning_score else "Lose"
            player_side = SCORE_FONT.render(f'{result1}', True, WHITE)
            self.screen.blit(player_side, (self.get_center_pos(player_side), self.ui_starting_y + 100))
            enemy_side = SCORE_FONT.render(f'{result2}', True, WHITE)
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
        if elapsed_time > 1000:
            self._spawn_ball()
            self.start_time = None

    def handle_score(self):
        if self.ball is not None:
            if self.ball.rect.right < 0:
                if not self.ball.scored:
                    self.ball.scored = True
                    self.enemy_score += 1
                if not self.game_over:
                    self.respawn_ball()
            if self.ball.rect.left > SCREEN_WIDTH:
                if not self.ball.scored:
                    self.ball.scored = True
                    self.player_score += 1
                if not self.game_over:
                    self.respawn_ball()

        if (self.player_score == self.winning_score or
                self.enemy_score == self.winning_score):
            self.game_over = True

    def handle_collisions(self):
        if self.ball is not None:
            if (self.ball.rect.colliderect(self.paddle1.rect) or
                    self.ball.rect.colliderect(self.paddle2.rect)):
                self.ball.has_bounced = True
                self.ball.dx *= -1
            if (self.ball.rect.top < 0 or
                    self.ball.rect.bottom > SCREEN_HEIGHT):
                self.ball.dy *= -1

            if self.ball.has_bounced:
                self.ball.dx = self.ball.dx / abs(self.ball.dx) * self.ball_speed

    def update(self):
        if self.ball is None:
            self.respawn_ball()

        if not self.game_over:
            self.paddle1.update_paddle1()
            self.paddle2.update_paddle2()
            if self.ball is not None:
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


def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == '__main__':
    main()
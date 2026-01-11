import pygame
import random
from settings import *

pygame.init()


def draw_window(score, health, ball, paddle):
    screen.fill(BG_COLOR)

    score_text = main_window_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (15, 15))

    health_text = main_window_font.render(f"Health: {health}", True, WHITE)
    screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 15, 15))

    pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_SIZE / 2)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    pygame.display.update()


def handle_ball(ball, ball_dx, ball_dy, paddle, health):
    ball.x += ball_dx
    ball.y += ball_dy

    if ball.left <= 0:
        ball_dx *= -1
        ball.left = 0
    if ball.right >= SCREEN_WIDTH:
        ball_dx *= -1
        ball.right = SCREEN_WIDTH
    if ball.top <= 0:
        ball_dy *= -1
        ball.top = 0

    if ball.colliderect(paddle):
        ball_dy *= -1

    if ball.bottom >= SCREEN_HEIGHT:
        health -= 1
        spawn_ball(ball)

    return ball_dx, ball_dy, health


def handle_paddle(paddle):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and paddle.x > 0:
        paddle.x -= PADDLE_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and paddle.x < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle.x += PADDLE_SPEED


def spawn_ball(ball):
    ball.x = (SCREEN_WIDTH - BALL_SIZE) // 2
    ball.y = SCREEN_HEIGHT - 70


def main():
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40
    paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
    spawn_ball(ball)

    ball_dx = random.choice([-4, 4])
    ball_dy = -5

    score = 0
    health = 3

    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_paddle(paddle)
        ball_dx, ball_dy, health = handle_ball(ball, ball_dx, ball_dy, paddle, health)
        draw_window(score, health, ball, paddle)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
import random
from settings import *

pygame.init()


def draw_window(paddle, score):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    score_text = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, 15))

    pygame.display.update()


def handle_movement(paddle):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and paddle.x > 0:
        paddle.x -= PADDLE_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and paddle.x < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle.x += PADDLE_SPEED


def main():
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40
    paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    score = 0

    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_movement(paddle)
        draw_window(paddle, score)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
import random
from settings import *

pygame.init()

def draw_screen(score, health, ball, paddle, game_over):
    screen.fill(BG_COLOR)

    score_text = main_window_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (15, 15))

    health_text = main_window_font.render(f"Health: {health}", True, WHITE)
    screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 15, 15))

    pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_SIZE / 2)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    if game_over:
        show_game_over()

    pygame.display.update()


def show_game_over():
    game_over_text = game_over_font.render(":(", True, WHITE)
    game_over_text_x = (SCREEN_WIDTH - game_over_text.get_width()) // 2 
    game_over_text_y = (SCREEN_HEIGHT // 2) - game_over_text.get_height()
    screen.blit(game_over_text,(game_over_text_x, game_over_text_y))

    instructions_text = subtext_font.render("Press R to restart | ESC to quit", True, SUBTEXT_COLOR)
    instructions_text_x = (SCREEN_WIDTH - instructions_text.get_width()) // 2
    instructions_text_y = (SCREEN_HEIGHT // 2) + instructions_text.get_height() + 10
    screen.blit(instructions_text, (instructions_text_x, instructions_text_y))


def handle_ball(move_ball, ball, ball_dx, ball_dy, paddle, health, game_over):
    if move_ball:
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
            if ball_dy > 0:
                ball.bottom = paddle.top
                ball_dy *= -1
            else:
                ball_dy *= -1
    
        if ball.top >= SCREEN_HEIGHT:
            health -= 1

            if health == 0:
                pygame.mixer.music.stop()
                game_over_sfx.play()
                game_over = True

            ball_dx, ball_dy, move_ball = respawn_ball(ball, paddle)

    return ball_dx, ball_dy, move_ball, health, game_over


def handle_entities(paddle, ball, move_ball):
    handle_entities_movement(paddle, paddle)

    if not move_ball:
        handle_entities_movement(paddle, ball)


def handle_entities_movement(paddle, entity):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and paddle.x > 0:
        entity.x -= PADDLE_SPEED

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and paddle.x < SCREEN_WIDTH - PADDLE_WIDTH:
        entity.x += PADDLE_SPEED


def respawn_ball(ball, paddle):
    ball.centerx = paddle.centerx
    ball.bottom = paddle.top - 5
    
    ball_dx = random.choice([-4, 4])
    ball_dy = -5
    move_ball = False

    return ball_dx, ball_dy, move_ball


def restart_game():
    pygame.mixer.music.play(-1)

    ball_dx = random.choice([-4, 4])
    ball_dy = -5
    move_ball = False

    score = 0
    health = 3
    game_over = False

    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40
    paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
    respawn_ball(ball, paddle)

    return paddle, ball, ball_dx, ball_dy, move_ball, score, health, game_over


def main():
    pygame.mixer.music.play(-1)

    ball_dx = random.choice([-4, 4])
    ball_dy = -5
    move_ball = False

    score = 0
    health = 3
    game_over = False

    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40
    paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
    respawn_ball(ball, paddle)

    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not move_ball:
                    move_ball = True

                if event.key == pygame.K_r and game_over:
                    paddle, ball, ball_dx, ball_dy, move_ball, score, health, game_over = restart_game()

                if event.key == pygame.K_ESCAPE and game_over:
                    running = False
        
        if not game_over:
            handle_entities(paddle, ball, move_ball)
            ball_dx, ball_dy, move_ball, health, game_over = handle_ball(
                move_ball, ball, ball_dx,
                ball_dy, paddle, health, game_over
            )
        draw_screen(score, health, ball, paddle, game_over)

    pygame.quit()


if __name__ == "__main__":
    main()
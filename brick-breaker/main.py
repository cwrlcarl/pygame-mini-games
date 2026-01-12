import pygame
import random
from settings import *

pygame.init()

def draw_screen(game_state):
    screen.fill(BG_COLOR)

    score_text = main_window_font.render(f"Score: {game_state['score']:04d}", True, WHITE)
    screen.blit(score_text, (15, 15))

    health_text = main_window_font.render(f"Health: {game_state['health']}", True, WHITE)
    screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 15, 15))

    for brick in game_state['bricks']:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    pygame.draw.circle(screen, BALL_COLOR, game_state['ball'].center, BALL_SIZE / 2)
    pygame.draw.rect(screen, PADDLE_COLOR, game_state['paddle'])

    if game_state['game_over']:
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


def handle_ball_collisions(game_state):
    if game_state['move_ball']:
        bricks = game_state['bricks']
        paddle = game_state['paddle']
        ball = game_state['ball']

        ball.x += game_state['ball_dx']
        ball.y += game_state['ball_dy']

        # brick collision
        for brick in bricks:
            if ball.colliderect(brick):
                game_state['score'] += 50
                game_state['ball_dy'] *= -1
                bricks.remove(brick)

        # paddle collision
        if ball.colliderect(paddle):
            if game_state['ball_dy'] > 0:
                ball.bottom = paddle.top
                game_state['ball_dy'] *= -1
            else:
                game_state['ball_dy'] *= -1

        # wall collision
        if ball.left <= 0:
            game_state['ball_dx'] *= -1
            ball.left = 0
        if ball.right >= SCREEN_WIDTH:
            game_state['ball_dx'] *= -1
            ball.right = SCREEN_WIDTH
        if ball.top <= 0:
            game_state['ball_dy'] *= -1
            ball.top = 0
        if ball.top >= SCREEN_HEIGHT:
            game_state['health'] -= 1

            if game_state['health'] == 0:
                pygame.mixer.music.stop()
                game_over_sfx.play()
                game_state['game_over'] = True

            respawn_ball(game_state)


def handle_entities(game_state):
    paddle = game_state['paddle']
    ball = game_state['ball']   

    handle_entities_movement(paddle, paddle)

    if not game_state['move_ball']:
        handle_entities_movement(paddle, ball)


def handle_entities_movement(paddle, entity):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and paddle.x > 0:
        entity.x -= PADDLE_SPEED

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and paddle.x < SCREEN_WIDTH - PADDLE_WIDTH:
        entity.x += PADDLE_SPEED


def respawn_ball(game_state):
    paddle = game_state['paddle']
    ball = game_state['ball']  

    ball.centerx = paddle.centerx
    ball.bottom = paddle.top - 5
    
    game_state['ball_dx'] = random.choice([-4, 4])
    game_state['ball_dy'] = -5
    game_state['move_ball'] = False


def create_game_state():
    pygame.mixer.music.play(-1)
    
    row_width = (BRICK_WIDTH * BRICK_COLUMN + BRICK_GAP * (BRICK_COLUMN - 1))
    bricks = []
    
    for row in range(BRICK_ROW):
        for col in range(BRICK_COLUMN):
            brick_x = col * (BRICK_WIDTH + BRICK_GAP) + (SCREEN_WIDTH - row_width) // 2
            brick_y = row * (BRICK_HEIGHT + BRICK_GAP) + 50

            brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick)

    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40
    paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)

    game_state = {
        'bricks': bricks,
        'paddle': paddle,
        'ball': ball,
        'ball_dx': random.choice([-4, 4]),
        'ball_dy': -5,
        'move_ball': False,
        'score': 0,
        'health': 3,
        'game_over': False
    }

    respawn_ball(game_state)
    return game_state


def main():
    game_state = create_game_state()

    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_state['move_ball']:
                    game_state['move_ball'] = True

                if event.key == pygame.K_r and game_state['game_over']:
                    game_state = create_game_state()

                if event.key == pygame.K_ESCAPE and game_state['game_over']:
                    running = False
        
        if not game_state['game_over']:
            handle_entities(game_state)
            handle_ball_collisions(game_state)
            
        draw_screen(game_state)

    pygame.quit()


if __name__ == "__main__":
    main()
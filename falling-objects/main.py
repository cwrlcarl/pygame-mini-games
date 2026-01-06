import pygame
import random
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 570, 400
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the flying ahh object")

main_screen_font = pygame.font.SysFont("Monocraft", 17)
game_over_font = pygame.font.SysFont("Monocraft", 80)
subtext_font = pygame.font.SysFont("Monocraft", 13)

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
catch_sfx = os.path.join(ASSETS_DIR, 'catch-sfx.wav')
fall_sfx = os.path.join(ASSETS_DIR, 'fall-sfx.wav')
game_over_sfx = os.path.join(ASSETS_DIR, 'game-over-sfx.ogg')

catch_sfx = pygame.mixer.Sound(catch_sfx)
fall_sfx = pygame.mixer.Sound(fall_sfx)
game_over_sfx = pygame.mixer.Sound(game_over_sfx)

BG_COLOR = (0, 0, 0)
MAIN_TEXT_COLOR = (255, 255, 255)
SUBTEXT_COLOR = (171, 171, 171)
PLAYER_COLOR = (224, 108, 152)
OBJECT_COLOR = (255, 151, 33)

PLAYER_WIDTH, PLAYER_HEIGHT = 70, 15
PLAYER_SPEED = 4

X_POS, Y_POS = random.randint(0, SCREEN_WIDTH - 50), -100
RADIUS = 20
FALL_SPEED = 5


def draw_window(player_rect, object_rect, score, health, game_over):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.draw.circle(screen, OBJECT_COLOR, object_rect.center, RADIUS)

    score_text = main_screen_font.render(f"Score: {score}", True, MAIN_TEXT_COLOR)
    screen.blit(score_text, (15, 10))

    health_text = main_screen_font.render(f"Health: {health}", True, MAIN_TEXT_COLOR)
    screen.blit(health_text, (15, 35))

    if game_over:
        show_game_over()
        
    pygame.display.update()


def show_game_over():
    game_over_text = game_over_font.render(":(", True, MAIN_TEXT_COLOR)
    game_over_text_x = (SCREEN_WIDTH - game_over_text.get_width()) // 2 
    game_over_text_y = (SCREEN_HEIGHT // 2) - game_over_text.get_height() - 5
    screen.blit(game_over_text,(game_over_text_x, game_over_text_y))
    
    instructions_text = subtext_font.render("Press R to restart | ESC to quit", True, SUBTEXT_COLOR)
    instructions_text_x = (SCREEN_WIDTH - instructions_text.get_width()) // 2
    instructions_text_y = (SCREEN_HEIGHT // 2) + instructions_text.get_height() + 5
    screen.blit(instructions_text, (instructions_text_x, instructions_text_y))


def handle_movement(player_rect):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.x > 0:
        player_rect.x -= PLAYER_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_SPEED


def handle_object(object_rect, player_rect, score, health, game_over):
    object_rect.y += FALL_SPEED

    if object_rect.y > SCREEN_HEIGHT:
        health -= 1
        reset_object(object_rect)
        fall_sfx.play()

        if health <= 0:
            game_over = True
            game_over_sfx.play()

    if player_rect.colliderect(object_rect):
        score += 10
        reset_object(object_rect)
        catch_sfx.play()
    
    return score, health, game_over


def reset_object(object_rect):
    object_rect.x = random.randint(0, SCREEN_WIDTH - RADIUS * 2)
    object_rect.y = Y_POS


def main():
    player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 20

    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    object_rect = pygame.Rect(X_POS, Y_POS, RADIUS * 2, RADIUS * 2)
    
    score = 0
    health = 3
    game_over = False
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    main()
                    return

                if event.key == pygame.K_ESCAPE and game_over:
                    running = False
        
        if not game_over:
            score, health, game_over = handle_object(
                object_rect, player_rect,
                score, health, game_over
            )
            handle_movement(player_rect)

        draw_window(
            player_rect, object_rect,
            score, health, game_over
        )

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
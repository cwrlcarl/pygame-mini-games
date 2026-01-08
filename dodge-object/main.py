import pygame
import random
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 450
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the falling ahh object")

score_font = pygame.font.SysFont("Monocraft", 17)
game_over_font = pygame.font.SysFont("Monocraft", 80)
subtext_font = pygame.font.SysFont("Monocraft", 12)

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
bg_music = os.path.join(ASSETS_DIR, 'bg-music.mp3')
game_over_sfx = os.path.join(ASSETS_DIR, 'game-over-sfx.ogg')

pygame.mixer.music.load(bg_music)
pygame.mixer.music.set_volume(0.3)
game_over_sfx = pygame.mixer.Sound(game_over_sfx)

BG_COLOR = (255, 255, 255)
MAIN_TEXT_COLOR = (22, 22, 23)
SUBTEXT_COLOR = (73, 73, 77)
PLAYER_COLOR = (73, 73, 209)
OBJECT_COLOR = (209, 73, 73)

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
PLAYER_SPEED = 4

RADIUS = 20
FALL_SPEED = 7
SPAWN_Y = -100


def draw_window(player_rect, object_rect, score, high_score, game_over):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.draw.circle(screen, OBJECT_COLOR, object_rect.center, RADIUS)
    
    time_text = score_font.render(f"Score: {score:.0f}", True, MAIN_TEXT_COLOR)
    screen.blit(time_text, (15, 12))

    high_score_text = score_font.render(f"High Score: {high_score:.0f}", True, MAIN_TEXT_COLOR)
    screen.blit(high_score_text, (15, 40))

    if game_over:
        show_game_over()

    pygame.display.update()


def show_game_over():
    game_over_text = game_over_font.render(":(", True, MAIN_TEXT_COLOR)
    game_over_text_x = (SCREEN_WIDTH - game_over_text.get_width()) // 2 
    game_over_text_y = (SCREEN_HEIGHT // 2) - game_over_text.get_height()
    screen.blit(game_over_text,(game_over_text_x, game_over_text_y))

    instructions_text = subtext_font.render("Press R to restart | ESC to quit", True, SUBTEXT_COLOR)
    instructions_text_x = (SCREEN_WIDTH - instructions_text.get_width()) // 2
    instructions_text_y = (SCREEN_HEIGHT // 2) + instructions_text.get_height() + 10
    screen.blit(instructions_text, (instructions_text_x, instructions_text_y))


def handle_movement(player_rect):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.x > 0:
        player_rect.x -= PLAYER_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_SPEED


def handle_object(object_rect, player_rect, fall_speed, game_over):
    object_rect.y += fall_speed

    if object_rect.y > SCREEN_HEIGHT:
        reset_object(object_rect)

    if player_rect.colliderect(object_rect) and not game_over:
        game_over = True
        game_over_sfx.play()
        pygame.mixer.music.stop()

    return game_over


def reset_game():
    pygame.mixer.music.play(-1)

    player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

    object_rect = pygame.Rect(0, SPAWN_Y, RADIUS * 2, RADIUS * 2)
    reset_object(object_rect)

    score = 0
    game_over = False
    fall_speed = FALL_SPEED

    return player_rect, object_rect, score, fall_speed, game_over


def reset_object(object_rect):
    object_rect.x = random.randint(0, SCREEN_WIDTH - RADIUS * 2)
    object_rect.y = SPAWN_Y


def main():
    pygame.mixer.music.play(-1)

    player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

    object_rect = pygame.Rect(0, SPAWN_Y, RADIUS * 2, RADIUS * 2)
    reset_object(object_rect)

    score = 0
    high_score = 0
    fall_speed = FALL_SPEED
    next_speed_increase = 10
    game_over = False

    clock = pygame.time.Clock()
    running = True
    
    while running:
        dt = clock.tick(FPS)

        if score >= next_speed_increase:
            fall_speed += 1
            next_speed_increase += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    player_rect, object_rect, score, fall_speed, game_over = reset_game()
                
                if event.key == pygame.K_ESCAPE and game_over:
                    running = False

        if not game_over:
            game_over = handle_object(object_rect, player_rect, fall_speed, game_over)
            handle_movement(player_rect)
            score += dt / 1000
        else:
            if score > high_score:
                high_score = score
            
        draw_window(player_rect, object_rect, score, high_score, game_over)

    pygame.quit()


if __name__ == "__main__":
    main()
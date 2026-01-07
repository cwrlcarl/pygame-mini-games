import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the falling ahh object")

time_font = pygame.font.SysFont("Monocraft", 17)
game_over_font = pygame.font.SysFont("Monocraft", 80)
subtext_font = pygame.font.SysFont("Monocraft", 12)

BG_COLOR = (240, 240, 245)
MAIN_TEXT_COLOR = (22, 22, 23)
SUBTEXT_COLOR = (73, 73, 77)
PLAYER_COLOR = (73, 73, 209)
OBJECT_COLOR = (209, 73, 73)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_SPEED = 4


def draw_window(player_rect, score, game_over):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    
    time_text = time_font.render(f"Time: {score}", True, MAIN_TEXT_COLOR)
    screen.blit(time_text, (15, 15))

    if game_over:
        game_over_text = game_over_font.render(":(", True, MAIN_TEXT_COLOR)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2,
                                     (SCREEN_HEIGHT - game_over_text.get_height()) // 2))

    pygame.display.update()


def handle_movement(player_rect):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.x > 0:
        player_rect.x -= PLAYER_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_SPEED


def main():
    player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

    score = 0
    game_over = False

    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(player_rect, score, game_over)
        handle_movement(player_rect)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
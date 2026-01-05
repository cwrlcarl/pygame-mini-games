import pygame
import random

pygame.init()

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the flying ahh object")
screen_font = pygame.font.SysFont("Monocraft", 17)

PLAYER_WIDTH, PLAYER_HEIGHT = 70, 15
PLAYER_SPEED = 4

X_POS, Y_POS = random.randint(0, SCREEN_WIDTH - 50), -50
RADIUS = 20
FALL_SPEED = 3

BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
PLAYER_COLOR = (224, 108, 152)
OBJECT_COLOR = (255, 151, 33)


def draw_window(player_rect, object_rect, score):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.draw.circle(screen, OBJECT_COLOR, object_rect.center, RADIUS)

    score_text = screen_font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (15, 10))

    pygame.display.update()


def handle_movement(player_rect):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.x > 0:
        player_rect.x -= PLAYER_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_SPEED


def handle_object(object_rect, player_rect, score):
    object_rect.y += FALL_SPEED

    if object_rect.y > SCREEN_HEIGHT:
        reset_object(object_rect)

    if player_rect.colliderect(object_rect):
        score += 10
        reset_object(object_rect)
    
    return score


def reset_object(object_rect):
    object_rect.x = random.randint(0, SCREEN_WIDTH - RADIUS * 2)
    object_rect.y = Y_POS


def main():
    score = 0
    lives = 3
    
    player_rect = pygame.Rect(((SCREEN_WIDTH // 2) - (PLAYER_WIDTH // 2),
                                SCREEN_HEIGHT - PLAYER_HEIGHT,
                                PLAYER_WIDTH, PLAYER_HEIGHT))
    
    object_rect = pygame.Rect((X_POS, Y_POS,
                               RADIUS * 2, RADIUS * 2))
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score = handle_object(object_rect, player_rect, score)
        handle_movement(player_rect)
        draw_window(player_rect, object_rect, score)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
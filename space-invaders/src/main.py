import pygame
from settings import *
from classes import *
from mechanics import *

def draw_game_screen(screen, game_state, bg_image, bg_width, bg_height):
    for x in range(0, SCREEN_WIDTH, bg_width):
        for y in range(0, SCREEN_HEIGHT, bg_height):
            screen.blit(bg_image, (x, y))

    for meteor in game_state['meteors']:
        meteor.draw(screen)

    game_state['player'].draw(screen)

    for player_bullet in game_state['player_bullets']:
        player_bullet.draw(screen)

    for enemy in game_state['enemies']:
        enemy.draw(screen)

    for enemy_bullet in game_state['enemy_bullets']:
        enemy_bullet.draw(screen)


def draw_game_ui(screen, game_state):
    screen.blit(HEALTH_ICON, HEALTH_ICON_RECT)
    screen.blit(NUMERAL_X, NUMERAL_X_RECT)
    if game_state['health'] == 3:
        draw_health(screen, NUMERAL_IMGS[3])
    elif game_state['health'] == 2:
        draw_health(screen, NUMERAL_IMGS[2])
    elif game_state['health'] == 1:
        draw_health(screen, NUMERAL_IMGS[1])
    elif game_state['health'] == 0:
        draw_health(screen, NUMERAL_IMGS[0])

    score_text = MAIN_FONT.render(f"{game_state['score']:05d}", True, WHITE)
    screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, 20))
    high_score_text = MAIN_FONT.render(f"HIGH: {game_state['high_score']}", True, WHITE)
    screen.blit(high_score_text, ((SCREEN_WIDTH - high_score_text.get_width()) - 30, 20))

    if game_state['game_over']:
        game_over_text = GAME_OVER_FONT.render(":(", True, WHITE)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2,
                                     (SCREEN_HEIGHT - game_over_text.get_height()) // 2))

        screen.blit(GAME_OVER_UI, ((SCREEN_WIDTH - GAME_OVER_UI.get_width()) // 2,
                              (SCREEN_HEIGHT - GAME_OVER_UI.get_height()) // 2))


def draw_health(screen, numeral_image):
    screen.blit(numeral_image, NUMERAL_IMGS_RECT)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load(BG_IMAGE_PATH).convert()
    bg_width, bg_height = bg_image.get_size()
    pygame.display.set_caption("Space Invaders 🚀")

    game_state = create_game_state()
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Thanks for playing!")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_state['game_over']:
                    if len(game_state['player_bullets']) < MAX_PLAYER_BULLETS:
                        LASER_SFX.play()
                        player_bullet = PlayerBullet(x=game_state['player'].rect.centerx, y=game_state['player'].rect.y)
                        game_state['player_bullets'].append(player_bullet)

                if event.key == pygame.K_r and game_state['game_over']:
                    game_state = create_game_state(game_state['high_score'])

                if event.key == pygame.K_ESCAPE and game_state['game_over']:
                    running = False
                    print("Thanks for playing!")

        if not game_state['game_over']:
            show_new_wave(game_state)

            bullets_hit_enemies(game_state)
            enemy_bullets_hit_player(game_state)
            enemies_hit_player(game_state)

            game_state = handle_enemy_bullets(game_state)
            handle_off_screen_bullets(game_state)

            handle_enemy_movement(game_state)
            handle_meteor_spawn(game_state)

            if not game_state['game_over']:
                update_entities(game_state)
        else:
            show_high_score(game_state)

        draw_game_screen(screen, game_state, bg_image, bg_width, bg_height)
        draw_game_ui(screen, game_state)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
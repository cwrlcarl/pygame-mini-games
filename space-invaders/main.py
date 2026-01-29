import pygame
import random
from settings import *
from classes import *


def draw_game_ui(screen, game_state):
    score_text = MAIN_FONT.render(f"Score: {game_state['score']:05d}", True, WHITE)
    screen.blit(score_text, (50, 20))

    health_text = MAIN_FONT.render(f"Health: {game_state['health']}", True, WHITE)
    screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 50, 20))

    if game_state['game_over']:
        game_over_text = GAME_OVER_FONT.render(":(", True, WHITE)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2,
                                     (SCREEN_HEIGHT - game_over_text.get_height()) // 2))


def create_game_state():
    pygame.init()
    pygame.mixer.music.play(-1)

    player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT - PLAYER_HEIGHT)

    game_state = {
        'player': player,
        'player_bullets': [],
        'enemies': [],
        'enemy_bullets': [],
        'last_enemy_shot': pygame.time.get_ticks(),
        'enemy_direction': 1,
        'enemy_hit_wall': False,
        'score': 0,
        'health': 3,
        'game_over': False
    }

    row_width = (ENEMY_WIDTH * ENEMY_COLS) + (ENEMY_COL_GAP * (ENEMY_COLS - 1))
    start_x = (SCREEN_WIDTH - row_width) // 2 + ENEMY_WIDTH // 2

    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            x = col * (ENEMY_WIDTH + ENEMY_COL_GAP) + start_x
            y = row * (ENEMY_HEIGHT + ENEMY_ROW_GAP) + ENEMY_OFFSET
            enemy = Enemy(x=x, y=y)
            game_state['enemies'].append(enemy)

    return game_state


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_state['game_over']:
                    if len(game_state['player_bullets']) < MAX_PLAYER_BULLETS:
                        LASER_SFX.play()
                        player_bullet = PlayerBullet(x=game_state['player'].rect.centerx, y=game_state['player'].rect.y)
                        game_state['player_bullets'].append(player_bullet)

                if event.key == pygame.K_r and game_state['game_over']:
                    game_state = create_game_state()

                if event.key == pygame.K_ESCAPE and game_state['game_over']:
                    running = False

        if not game_state['game_over']:
            # player bullet and enemy collision
            for player_bullet in game_state['player_bullets'][:]:
                for enemy in game_state['enemies'][:]:
                    if player_bullet.rect.colliderect(enemy.rect):
                        ZAP_SFX.play()
                        game_state['score'] += 50
                        game_state['player_bullets'].remove(player_bullet)
                        game_state['enemies'].remove(enemy)

            # enemy bullet and player collision
            for enemy_bullet in game_state['enemy_bullets'][:]:
                if enemy_bullet.rect.colliderect(game_state['player'].rect):
                    HIT_SFX.play()
                    game_state['health'] -= 1
                    game_state['enemy_bullets'].remove(enemy_bullet)
                    if game_state['health'] == 0:
                        GAME_OVER_SFX.play()
                        pygame.mixer.music.stop()
                        game_state['game_over'] = True

            # enemy and player collision
            for enemy in game_state['enemies']:
                if game_state['player'].rect.colliderect(enemy.rect):
                    GAME_OVER_SFX.play()
                    pygame.mixer.music.stop()
                    game_state['game_over'] = True

            # off-screen bullets
            for player_bullet in game_state['player_bullets'][:]:
                if player_bullet.rect.y < 0:
                    game_state['player_bullets'].remove(player_bullet)
            for enemy_bullet in game_state['enemy_bullets'][:]:
                if enemy_bullet.rect.y > SCREEN_HEIGHT:
                    game_state['enemy_bullets'].remove(enemy_bullet)

            # enemy shooting
            time_now = pygame.time.get_ticks()
            if time_now - game_state['last_enemy_shot'] > ENEMY_BULLET_COOLDOWN \
            and len(game_state['enemy_bullets']) < MAX_ENEMY_BULLETS \
            and len(game_state['enemies']) > 0:
                enemy_shooting = random.choice(game_state['enemies'])
                enemy_bullet = EnemyBullet(x=enemy_shooting.rect.centerx, y=enemy_shooting.rect.bottom)
                game_state['enemy_bullets'].append(enemy_bullet)
                game_state['last_enemy_shot'] = time_now

            # enemy direction
            for enemy in game_state['enemies']:
                if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                    game_state['enemy_hit_wall'] = True

            if game_state['enemy_hit_wall']:
                game_state['enemy_direction'] *= -1
                for enemy in game_state['enemies']:
                    enemy.rect.y += ENEMY_DY
                    game_state['enemy_hit_wall'] = False

            # update
            if not game_state['game_over']:
                game_state['player'].update()

                for player_bullet in game_state['player_bullets']:
                    player_bullet.update()

                for enemy in game_state['enemies']:
                    enemy.update(game_state['enemy_direction'])

                for enemy_bullet in game_state['enemy_bullets']:
                    enemy_bullet.update()

        # draw
        for x in range(0, SCREEN_WIDTH, bg_width):
            for y in range(0, SCREEN_HEIGHT, bg_height):
                screen.blit(bg_image, (x, y))

        game_state['player'].draw(screen)

        for player_bullet in game_state['player_bullets']:
            player_bullet.draw(screen)

        for enemy in game_state['enemies']:
            enemy.draw(screen)

        for enemy_bullet in game_state['enemy_bullets']:
            enemy_bullet.draw(screen)

        draw_game_ui(screen, game_state)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
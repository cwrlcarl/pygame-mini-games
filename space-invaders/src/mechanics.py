import pygame
import random
from settings import *
from classes import *

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


def bullets_hit_enemies(game_state):
    for player_bullet in game_state['player_bullets'][:]:
        for enemy in game_state['enemies'][:]:
            if player_bullet.rect.colliderect(enemy.rect):
                ZAP_SFX.play()
                game_state['score'] += 50
                game_state['player_bullets'].remove(player_bullet)
                game_state['enemies'].remove(enemy)


def enemy_bullets_hit_player(game_state):
    for enemy_bullet in game_state['enemy_bullets'][:]:
        if enemy_bullet.rect.colliderect(game_state['player'].rect):
            HIT_SFX.play()
            game_state['health'] -= 1
            game_state['enemy_bullets'].remove(enemy_bullet)
            if game_state['health'] == 0:
                GAME_OVER_SFX.play()
                pygame.mixer.music.stop()
                game_state['game_over'] = True


def enemies_hit_player(game_state):
    for enemy in game_state['enemies']:
        if game_state['player'].rect.colliderect(enemy.rect):
            GAME_OVER_SFX.play()
            pygame.mixer.music.stop()
            game_state['game_over'] = True


def handle_enemy_bullets(game_state):
    time_now = pygame.time.get_ticks()
    if time_now - game_state['last_enemy_shot'] > ENEMY_BULLET_COOLDOWN \
            and len(game_state['enemy_bullets']) < MAX_ENEMY_BULLETS \
            and len(game_state['enemies']) > 0:
        enemy_shooting = random.choice(game_state['enemies'])
        enemy_bullet = EnemyBullet(x=enemy_shooting.rect.centerx, y=enemy_shooting.rect.bottom)
        game_state['enemy_bullets'].append(enemy_bullet)
        game_state['last_enemy_shot'] = time_now

    return game_state


def handle_off_screen_bullets(game_state):
    for player_bullet in game_state['player_bullets'][:]:
        if player_bullet.rect.y < 0:
            game_state['player_bullets'].remove(player_bullet)
    for enemy_bullet in game_state['enemy_bullets'][:]:
        if enemy_bullet.rect.y > SCREEN_HEIGHT:
            game_state['enemy_bullets'].remove(enemy_bullet)


def handle_enemy_movement(game_state):
    for enemy in game_state['enemies']:
        if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
            game_state['enemy_hit_wall'] = True

    if game_state['enemy_hit_wall']:
        game_state['enemy_direction'] *= -1
        for enemy in game_state['enemies']:
            enemy.rect.y += ENEMY_DY
            game_state['enemy_hit_wall'] = False


def update_entities(game_state):
    game_state['player'].update()

    for player_bullet in game_state['player_bullets']:
        player_bullet.update()

    for enemy in game_state['enemies']:
        enemy.update(game_state['enemy_direction'])

    for enemy_bullet in game_state['enemy_bullets']:
        enemy_bullet.update()
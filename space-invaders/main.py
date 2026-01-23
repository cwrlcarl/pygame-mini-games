from encodings.cp862 import encoding_map

import pygame
import random
from settings import *


class Player:
    def __init__(self, x, y):
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class PlayerBullet:
    def __init__(self, x, y):
        self.image = BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemy:
    def __init__(self, x, y):
        self.image = random.choice(ENEMY_IMGS)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, direction):
        self.rect.x += ENEMY_SPEED * direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyBullet:
    def __init__(self, x, y):
        self.image = ENEMY_BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += ENEMY_BULLET_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    pygame.init()
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load(BG_IMAGE_PATH).convert()
    bg_width, bg_height = bg_image.get_size()
    pygame.display.set_caption("Space Invaders 🚀")

    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-PLAYER_HEIGHT)
    bullets = []
    enemies = []
    enemy_bullets = []
    enemy_direction = 1
    enemy_cooldown = 1000
    last_enemy_shot = pygame.time.get_ticks()
    score = 0
    health = 3

    row_width = (ENEMY_WIDTH * ENEMY_COLS) + (ENEMY_COL_GAP * (ENEMY_COLS - 1))
    start_x = (SCREEN_WIDTH - row_width) // 2 + ENEMY_WIDTH // 2

    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            x = col * (ENEMY_WIDTH + ENEMY_COL_GAP) + start_x
            y = row * (ENEMY_HEIGHT + ENEMY_ROW_GAP) + ENEMY_OFFSET

            enemy = Enemy(x=x, y=y)
            enemies.append(enemy)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(bullets) < MAX_BULLETS:
                        LASER_SFX.play()
                        bullet = PlayerBullet(x=player.rect.centerx, y=player.rect.y)
                        bullets.append(bullet)

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    score += 50
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        for bullet in bullets[:]:
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        for enemy_bullet in enemy_bullets[:]:
            if enemy_bullet.rect.y > SCREEN_HEIGHT:
                enemy_bullets.remove(enemy_bullet)

        for enemy in enemies:
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                enemy_direction *= -1
                break

        time_now = pygame.time.get_ticks()
        if time_now - last_enemy_shot > enemy_cooldown and len(enemy_bullets) < 5 and len(enemies) > 0:
            enemy_shooting = random.choice(enemies)
            enemy_bullet = EnemyBullet(x=enemy_shooting.rect.centerx, y=enemy_shooting.rect.y)
            enemy_bullets.append(enemy_bullet)
            last_enemy_shot = time_now

        for x in range(0, SCREEN_WIDTH, bg_width):
            for y in range(0, SCREEN_HEIGHT, bg_height):
                screen.blit(bg_image, (x, y))

        score_text = main_window_text.render(f"Score: {score:05d}", True, WHITE)
        screen.blit(score_text, (10, 10))

        health_text = main_window_text.render(f"Health: {health}", True, WHITE)
        screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 10, 10))

        player.update()
        player.draw(screen)

        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)

        for enemy in enemies:
            enemy.update(enemy_direction)
            enemy.draw(screen)

        for enemy_bullet in enemy_bullets:
            enemy_bullet.update()
            enemy_bullet.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
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
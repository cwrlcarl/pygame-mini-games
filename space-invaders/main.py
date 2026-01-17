import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.img = PLAYER_IMG
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.img, self.rect)


class Bullet:
    def __init__(self, x, y):
        self.img = BULLET_IMG
        self.rect = self.img.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.img, self.rect)


def main():
    pygame.init()
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders 🚀")

    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-PLAYER_HEIGHT)
    bullets = []

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
                        bullet = Bullet(x=player.rect.centerx, y=player.rect.y)
                        bullets.append(bullet)

        player.update()
        for bullet in bullets:
            bullet.update()

        for bullet in bullets[:]:
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        screen.fill(BG_COLOR)
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
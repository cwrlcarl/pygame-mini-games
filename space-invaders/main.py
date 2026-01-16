import pygame
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 540, 540
FPS = 60

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'img')
SHIP_PATH = os.path.join(IMG_DIR, 'blue-ship.png')

player_img = pygame.image.load(SHIP_PATH)
PLAYER_IMG = pygame.transform.scale_by(player_img, 0.75)
PLAYER_WIDTH = PLAYER_IMG.get_width()
PLAYER_HEIGHT = PLAYER_IMG.get_height()
PLAYER_SPEED = 5

BG_COLOR = (37, 35, 41)
WHITE = (242, 240, 245)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders 🚀")

    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()

        screen.fill(BG_COLOR)
        player.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
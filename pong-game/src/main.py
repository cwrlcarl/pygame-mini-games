import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pong Game')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.paddle1 = Paddle(50, SCREEN_HEIGHT // 2, (0, 0, 255))
        self.paddle2 = Paddle(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2, (255, 0, 0))
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def update(self):
        self.paddle1.update_paddle1()
        self.paddle2.update_paddle2()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.update()
            self.events()


class Paddle:
    def __init__(self, x, y, color):
        self.color = color
        self.width, self.height = 10, 80
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 7

    def update_paddle1(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if k[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def update_paddle2(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if k[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.rect = pygame.Rect(x, y, self.radius, self.radius)
        self.speed = 7

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.rect.center, self.radius)


def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == '__main__':
    main()
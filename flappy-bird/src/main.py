import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 540, 640
FPS = 60

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird 🐤")

        self.clock = pygame.time.Clock()
        self.running = True

        self.bird = Bird()

    def update(self):
        self.bird.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bird.draw(self.screen)
        pygame.display.update()


    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.is_jumping = True
                        self.bird.velocity = self.bird.jump_strength

            self.update()
            self.draw()


class Bird:
    def __init__(self):
        self.rect = pygame.Rect((0, 0, 35, 35))
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.color = (255, 255, 0)
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.is_jumping = False

    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
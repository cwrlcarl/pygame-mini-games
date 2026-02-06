from settings import SCREEN_WIDTH, SCREEN_HEIGHT, load_assets

class Bird:
    def __init__(self):
        self.image = load_assets()['sprites']['bird']
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.color = (255, 255, 0)
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -9
        self.is_jumping = False

    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
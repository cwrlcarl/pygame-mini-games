from settings import SCREEN_WIDTH, SCREEN_HEIGHT, load_assets

class Bird:
    def __init__(self):
        self.image = load_assets()['sprites']['bird']
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.y = float(self.rect.centery)
        self.color = (255, 255, 0)
        self.velocity = 0
        self.gravity = 0.4
        self.jump_strength = -7.5
        self.max_fall_speed = 10
        self.is_jumping = False

    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            if self.velocity > self.max_fall_speed:
                self.velocity = self.max_fall_speed
            self.y += self.velocity
            self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
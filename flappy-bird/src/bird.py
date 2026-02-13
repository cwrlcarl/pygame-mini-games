from settings import SCREEN_WIDTH, SCREEN_HEIGHT, load_assets

class Bird:
    def __init__(self):
        self.sprites = []
        for item in load_assets()['sprites']['bird']:
            self.sprites.append(item)

        self.wing_count = 0
        self.image = self.sprites[self.wing_count]
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

        self.wing_count += 0.25
        if self.wing_count >= len(self.sprites):
            self.wing_count = 0
        self.image = self.sprites[int(self.wing_count)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
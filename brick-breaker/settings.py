import pygame
import os

pygame.init()

# window
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker 🧱")


# texts
score_font = pygame.font.SysFont("Monocraft", 20)
game_over_font = pygame.font.SysFont("Monocraft", 80)
subtext_font = pygame.font.SysFont("Monocraft", 12)


# sounds
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
bg_music = os.path.join(ASSETS_DIR, 'bg-music.mp3')
game_over_sfx = os.path.join(ASSETS_DIR, 'game-over-sfx.ogg')

pygame.mixer.music.load(bg_music)
pygame.mixer.music.set_volume(0.3)
game_over_sfx = pygame.mixer.Sound(game_over_sfx)


# colors
BG_COLOR = (37, 35, 41)
WHITE = (242, 240, 245)
BALL_COLOR = (214, 56, 56)
PADDLE_COLOR = WHITE


# paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 10
PADDLE_SPEED = 5


# ball
BALL_SIZE = 20
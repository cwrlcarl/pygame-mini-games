import pygame
import os

pygame.font.init()
pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
FPS = 60
TEXT_FONT = pygame.font.SysFont('Monocraft', 50)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')
SPAWN_SFX = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'spawn.wav'))
WALL_HIT = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'wall-hit.wav'))
PADDLE_HIT = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'paddle-hit.wav'))
SCORE_SFX = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'score.wav'))
GAME_OVER_SFX = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'game-over.mp3'))

WHITE = (235, 237, 245)
BG_COLOR = (22, 23, 26)
DIVIDER_COLOR = (64, 64, 64)
PLAYER_PADDLE_COLOR = (51, 61, 196)
ENEMY_PADDLE_COLOR = (196, 51, 63)
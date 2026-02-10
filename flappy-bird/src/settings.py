import pygame
import os

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 550, 650
FPS = 60

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
AUDIO_DIR = os.path.join(ASSETS_DIR, 'audio')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')

score_font = pygame.font.SysFont("KenVector Future Regular", 35)

def load_assets():
    bottom_pipe = pygame.transform.scale_by(
        pygame.image.load(os.path.join(
            SPRITES_DIR, 'pipe-green.png')),1.6)
    top_pipe = pygame.transform.flip(bottom_pipe, False, True)

    return {
        'audio': {
            'die': pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'die.wav')),
            'hit': pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'hit.wav')),
            'point': pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'point.wav')),
            'swoosh': pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'swoosh.wav')),
            'wing': pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'wing.wav'))
        },
        'sprites': {
            'bird': pygame.transform.scale_by(
                pygame.image.load(os.path.join(SPRITES_DIR, 'yellowbird-downflap.png')),
                1.5
            ),
            'bottom_pipe': bottom_pipe,
            'top_pipe': top_pipe,
            'base': pygame.transform.scale_by(
                pygame.image.load(os.path.join(SPRITES_DIR, 'base.png')),
                1.3
            ),
            'background': pygame.transform.scale(
                pygame.image.load(os.path.join(SPRITES_DIR, 'background-day.png')),
                (SCREEN_WIDTH, SCREEN_HEIGHT)
            ),
            'message': pygame.image.load(os.path.join(SPRITES_DIR, 'message.png'))
        }
    }
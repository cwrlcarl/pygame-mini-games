import pygame
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 540, 640
FPS = 60

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
AUDIO_DIR = os.path.join(ASSETS_DIR, 'audio')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')

def load_assets():
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
            'pipe': pygame.image.load(os.path.join(SPRITES_DIR, 'pipe-green.png')),
            'base': pygame.image.load(os.path.join(SPRITES_DIR, 'base.png')),
            'background': pygame.transform.scale(
                pygame.image.load(os.path.join(SPRITES_DIR, 'background-day.png')),
                (SCREEN_WIDTH, SCREEN_HEIGHT))
        }
    }
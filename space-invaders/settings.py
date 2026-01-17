import pygame
import os

pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 540, 540
FPS = 60

# COLORS
BG_COLOR = (37, 35, 41)
WHITE = (242, 240, 245)

# PATHS
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'img')
AUDIO_DIR = os.path.join(ASSETS_DIR, 'audio')

# AUDIO
BG_MUSIC = os.path.join(AUDIO_DIR, 'space-invaders-bgm.mp3')
pygame.mixer.music.load(BG_MUSIC)
pygame.mixer.music.set_volume(0.3)

LASER_SFX_PATH = os.path.join(AUDIO_DIR, 'laser-sfx.ogg')
LASER_SFX = pygame.mixer.Sound(LASER_SFX_PATH)
LASER_SFX.set_volume(0.5)

# PLAYER
PLAYER_SPEED = 5
PLAYER_IMG_PATH = os.path.join(IMG_DIR, 'blue-ship.png')
_player_img = pygame.image.load(PLAYER_IMG_PATH)
PLAYER_IMG = pygame.transform.scale_by(_player_img, 0.75)
PLAYER_WIDTH = PLAYER_IMG.get_width()
PLAYER_HEIGHT = PLAYER_IMG.get_height()

# BULLET
BULLET_SPEED = 7
MAX_BULLETS = 3
BULLET_IMG_PATH = os.path.join(IMG_DIR, 'green-laser.png')
_bullet_img = pygame.image.load(BULLET_IMG_PATH)
BULLET_IMG = pygame.transform.scale_by(_bullet_img, 0.85)
BULLET_WIDTH = BULLET_IMG.get_width()
BULLET_HEIGHT = BULLET_IMG.get_height()

# ENEMY
ENEMY_IMG_PATH = os.path.join(IMG_DIR, 'black-enemy.png')
_enemy_img = pygame.image.load(ENEMY_IMG_PATH)
ENEMY_IMG = pygame.transform.scale_by(_enemy_img, 0.70)
ENEMY_WIDTH = ENEMY_IMG.get_width()
ENEMY_HEIGHT = ENEMY_IMG.get_height()
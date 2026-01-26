import pygame
import os

pygame.mixer.init()
pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
FPS = 60

# COLORS
BG_COLOR = (37, 35, 41)
WHITE = (242, 240, 245)

# TEXTS
MAIN_FONT = pygame.font.SysFont("Monocraft", 18)
GAME_OVER_FONT = pygame.font.SysFont("Monocraft", 60)

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

GAME_OVER_SFX_PATH = os.path.join(AUDIO_DIR, 'game-over-sfx.ogg')
GAME_OVER_SFX = pygame.mixer.Sound(GAME_OVER_SFX_PATH)

# BG IMAGE
BG_IMAGE_PATH = os.path.join(IMG_DIR, 'black-bg.png')

# PLAYER
PLAYER_SPEED = 5
PLAYER_IMG_PATH = os.path.join(IMG_DIR, 'blue-ship.png')
_player_img = pygame.image.load(PLAYER_IMG_PATH)
PLAYER_IMG = pygame.transform.scale_by(_player_img, 0.75)
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMG.get_size()

# PLAYER BULLET
BULLET_SPEED = 7
MAX_PLAYER_BULLETS = 1
BULLET_IMG_PATH = os.path.join(IMG_DIR, 'green-laser.png')
_bullet_img = pygame.image.load(BULLET_IMG_PATH)
BULLET_IMG = pygame.transform.scale_by(_bullet_img, 0.85)
BULLET_WIDTH, BULLET_HEIGHT = BULLET_IMG.get_size()

# ENEMY
ENEMY_SPEED = 1
ENEMY_DY = 20
ENEMY_ROWS, ENEMY_COLS  = 4, 7
ENEMY_ROW_GAP, ENEMY_COL_GAP = 30, 20
ENEMY_OFFSET = 80
ENEMY_IMGS = [
    pygame.transform.scale_by(
        pygame.image.load(os.path.join(IMG_DIR, f'enemy{i}.png')),
        0.50
    )
    for i in range(1, 5)
]
ENEMY_WIDTH, ENEMY_HEIGHT = ENEMY_IMGS[0].get_size()

# ENEMY BULLET
ENEMY_BULLET_SPEED = 4
MAX_ENEMY_BULLETS = 7
ENEMY_BULLET_COOLDOWN = 700
ENEMY_BULLET_IMG_PATH = os.path.join(IMG_DIR, 'red-laser.png')
_enemy_bullet_img = pygame.image.load(ENEMY_BULLET_IMG_PATH)
ENEMY_BULLET_IMG = pygame.transform.scale_by(_enemy_bullet_img, 0.30)
ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT = ENEMY_BULLET_IMG.get_size()
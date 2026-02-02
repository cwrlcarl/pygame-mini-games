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
MAIN_FONT = pygame.font.SysFont("KenVector Future Regular", 24)
GAME_OVER_FONT = pygame.font.SysFont("KenVector Future Regular", 60)

# PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

ZAP_SFX_PATH = os.path.join(AUDIO_DIR, 'zap-sfx.wav')
ZAP_SFX = pygame.mixer.Sound(ZAP_SFX_PATH)

HIT_SFX_PATH = os.path.join(AUDIO_DIR, 'hit-sfx.wav')
HIT_SFX = pygame.mixer.Sound(HIT_SFX_PATH)

GAME_OVER_SFX_PATH = os.path.join(AUDIO_DIR, 'game-over-sfx.ogg')
GAME_OVER_SFX = pygame.mixer.Sound(GAME_OVER_SFX_PATH)

# UI ICON
HEALTH_ICON_PATH =  os.path.join(IMG_DIR, 'player-health.png')
HEALTH_ICON = pygame.image.load(HEALTH_ICON_PATH)
HEALTH_ICON_RECT = HEALTH_ICON.get_rect(topleft=(30, 20))

NUMERAL_X_PATH = os.path.join(IMG_DIR, 'numeralx.png')
NUMERAL_X = pygame.image.load(NUMERAL_X_PATH)
NUMERAL_X_RECT = NUMERAL_X.get_rect(midleft=(HEALTH_ICON_RECT.right + 10, HEALTH_ICON_RECT.centery))

NUMERAL_IMGS = [
    pygame.image.load(os.path.join(IMG_DIR, f'numeral{i}.png'))
    for i in range(4)
]
NUMERAL_IMGS_RECT = NUMERAL_IMGS[0].get_rect(midleft=(NUMERAL_X_RECT.right + 10, HEALTH_ICON_RECT.centery))

# PLAYER
PLAYER_SPEED = 5
PLAYER_IMG_PATH = os.path.join(IMG_DIR, 'red-ship.png')
_player_img = pygame.image.load(PLAYER_IMG_PATH)
PLAYER_IMG = pygame.transform.scale_by(_player_img, 0.75)
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMG.get_size()

# PLAYER BULLET
BULLET_SPEED = 7
MAX_PLAYER_BULLETS = 100
BULLET_IMG_PATH = os.path.join(IMG_DIR, 'green-laser.png')
_bullet_img = pygame.image.load(BULLET_IMG_PATH)
BULLET_IMG = pygame.transform.scale_by(_bullet_img, 0.85)
BULLET_WIDTH, BULLET_HEIGHT = BULLET_IMG.get_size()

# ENEMY
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

# METEOR
METEOR_SPEED = 1
METEOR_SPAWN_INTERVAL = 3000
MAX_METEORS = 7
METEOR_IMGS = [
    pygame.image.load(os.path.join(IMG_DIR, f'grey-meteor{i}.png'))
    for i in range(8)
]
METEOR_WIDTH, METEOR_HEIGHT = METEOR_IMGS[0].get_size()

# BG IMAGE
BG_IMAGE_PATH = os.path.join(IMG_DIR, 'black-bg.png')

GAME_OVER_UI_PATH = os.path.join(IMG_DIR, 'game-over-ui.jpg')
_game_over_ui = pygame.image.load(GAME_OVER_UI_PATH)
GAME_OVER_UI = pygame.transform.scale_by(_game_over_ui, 0.30)
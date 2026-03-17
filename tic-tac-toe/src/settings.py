import pygame
import os

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 700
FPS = 60

PANEL_SIZE = 400
MARGIN = 100
GRID_TOP = 150
ROWS, COLS = 3, 3
CELL_SIZE = PANEL_SIZE // COLS
LINE_WIDTH = 5

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
X_IMG = os.path.join(ASSETS_DIR, 'x-img.png')
O_IMG = os.path.join(ASSETS_DIR, 'o-img.png')
TEXT_FONT = pygame.font.SysFont('GamePausedDEMO-Regular', 40)

TEXT_COLOR = (214, 216, 218)
LINE_COLOR = (106, 113, 124)
BG_COLOR = (36, 41, 46)
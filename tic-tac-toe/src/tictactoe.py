import pygame
from settings import *

class TicTacToe:
    def __init__(self):
        self.board = [[None]*3, [None]*3, [None]*3]
        self.turn = 'x'
        self.winner = None
        self.draw = None
        self.x_img = pygame.transform.scale(pygame.image.load(X_IMG), (CELL_SIZE, CELL_SIZE))
        self.o_img = pygame.transform.scale(pygame.image.load(O_IMG), (CELL_SIZE, CELL_SIZE))

    @staticmethod
    def draw_layout(screen):
        for i in range(1, ROWS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN, GRID_TOP + i * CELL_SIZE), (PANEL_SIZE + MARGIN, GRID_TOP + i * CELL_SIZE), LINE_WIDTH)
        for i in range(1, COLS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN + i * CELL_SIZE, GRID_TOP), (MARGIN + i * CELL_SIZE, GRID_TOP + PANEL_SIZE), LINE_WIDTH)

    def draw_XO(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                x = MARGIN + col * CELL_SIZE
                y = GRID_TOP + row * CELL_SIZE
                if self.board[row][col] == 'x':
                    screen.blit(self.x_img, (x, y))
                elif self.board[row][col] == 'o':
                    screen.blit(self.o_img, (x, y))
                    
    def handle_click(self, row, col):
        if self.board[row][col] is None:
            if self.turn == 'x':
                self.board[row][col] = 'x'
                self.turn = 'o'
            else:
                self.board[row][col] = 'o'
                self.turn = 'x'
            print(f'Board: {self.board}')
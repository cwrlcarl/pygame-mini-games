import pygame
from tictactoe import TicTacToe
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tictactoe = TicTacToe()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.tictactoe.draw_grid(self.screen)
        self.tictactoe.draw_XO(self.screen)
        self.tictactoe.render_turn_text(self.screen)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    row, col = (y - GRID_TOP) // CELL_SIZE, (x - MARGIN) // CELL_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS:
                        self.tictactoe.handle_click(row, col)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.events()
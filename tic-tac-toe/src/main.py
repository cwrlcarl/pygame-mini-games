import pygame
import os

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

TEXT_COLOR = (214, 216, 218)
LINE_COLOR = (106, 113, 124)
BG_COLOR = (36, 41, 46)


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
        self.tictactoe.draw_layout(self.screen)
        self.tictactoe.draw_XO(self.screen)
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


def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == '__main__':
    main()
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 700
FPS = 60

PANEL_SIZE = 400
MARGIN = 100
GRID_TOP = 150
ROWS, COLS = 3, 3
CELL_SIZE = PANEL_SIZE // COLS
LINE_WIDTH = 5
TEXT_COLOR = (214, 216, 218)
LINE_COLOR = (106, 113, 124)
BG_COLOR = (36, 41, 46)


class TicTacToe:
    def __init__(self):
        self.x_o = 'x'
        self.winner = None
        self.draw = None
        self.board = [[None]*3, [None]*3, [None]*3]

    @staticmethod
    def draw_layout(screen):
        for i in range(1, ROWS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN, GRID_TOP + i * CELL_SIZE), (PANEL_SIZE + MARGIN, GRID_TOP + i * CELL_SIZE), LINE_WIDTH)
        for i in range(1, COLS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN + i * CELL_SIZE, GRID_TOP), (MARGIN + i * CELL_SIZE, GRID_TOP + PANEL_SIZE), LINE_WIDTH)


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
        pygame.display.update()

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    row, col = (y - GRID_TOP) // CELL_SIZE, (x - MARGIN) // CELL_SIZE
                    print(f'Row{row} Col{col}')

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
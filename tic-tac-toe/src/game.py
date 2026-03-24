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
        self.x_img = pygame.transform.scale(pygame.image.load(X_IMG), (CELL_SIZE, CELL_SIZE))
        self.o_img = pygame.transform.scale(pygame.image.load(O_IMG), (CELL_SIZE, CELL_SIZE))
        self.winner = None
        self.line = None
        self.x_score = 0
        self.o_score = 0
        self.tictactoe = TicTacToe()

    def draw_grid(self):
        for i in range(1, ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (MARGIN, GRID_TOP + i * CELL_SIZE),
                             (PANEL_SIZE + MARGIN, GRID_TOP + i * CELL_SIZE), LINE_WIDTH)
        for i in range(1, COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (MARGIN + i * CELL_SIZE, GRID_TOP),
                             (MARGIN + i * CELL_SIZE, GRID_TOP + PANEL_SIZE), LINE_WIDTH)

    def draw_XO(self):
        for row in range(ROWS):
            for col in range(COLS):
                x = MARGIN + col * CELL_SIZE
                y = GRID_TOP + row * CELL_SIZE
                if self.tictactoe.get_board()[row][col] == 'x':
                    self.screen.blit(self.x_img, (x, y))
                elif self.tictactoe.get_board()[row][col] == 'o':
                    self.screen.blit(self.o_img, (x, y))

    def draw_winner(self):
        if self.line:
            line_type, line_index = self.line
            if line_type == 'row':
                pygame.draw.line(
                    self.screen, LINE_COLOR,
                    (MARGIN, GRID_TOP + line_index * CELL_SIZE + CELL_SIZE // 2),
                    (MARGIN + PANEL_SIZE, GRID_TOP + line_index * CELL_SIZE + CELL_SIZE // 2),
                    LINE_WIDTH)
            elif line_type == 'col':
                pygame.draw.line(
                    self.screen, LINE_COLOR,
                    (MARGIN + line_index * CELL_SIZE + CELL_SIZE // 2, GRID_TOP),
                    (MARGIN + line_index * CELL_SIZE + CELL_SIZE // 2, GRID_TOP + PANEL_SIZE),
                    LINE_WIDTH)
            elif line_type == 'diag' and line_index == 0:
                pygame.draw.line(
                    self.screen, LINE_COLOR,
                    (MARGIN + CELL_SIZE // 2, GRID_TOP + CELL_SIZE // 2),
                    (MARGIN + PANEL_SIZE - CELL_SIZE // 2, GRID_TOP + PANEL_SIZE - CELL_SIZE // 2),
                    LINE_WIDTH)
            elif line_type == 'diag' and line_index == 1:
                pygame.draw.line(
                    self.screen, LINE_COLOR,
                    (MARGIN + PANEL_SIZE - CELL_SIZE // 2, GRID_TOP + CELL_SIZE // 2),
                    (MARGIN + CELL_SIZE // 2, GRID_TOP + PANEL_SIZE - CELL_SIZE // 2),
                    LINE_WIDTH)

    def render_turn_text(self):
        if self.winner:
            turn_text = TEXT_FONT.render(f'{self.winner.upper()} Won', True, TEXT_COLOR)
        else:
            turn_text = TEXT_FONT.render(f'{self.tictactoe.get_turn()} Turn', True, TEXT_COLOR)
        
        self.screen.blit(
            turn_text, 
            ((SCREEN_WIDTH - turn_text.get_width()) // 2, 
            (GRID_TOP - turn_text.get_height()) // 2))

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        self.draw_XO()
        self.draw_winner()
        self.render_turn_text()
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.winner: return

                if event.button == 1:
                    x, y = event.pos
                    row, col = (y - GRID_TOP) // CELL_SIZE, (x - MARGIN) // CELL_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS:
                        self.tictactoe.handle_click(row, col)
                        winner, line = self.tictactoe.check_winner()
                        if winner and not self.winner:
                            self.winner = winner
                            self.line = line
                            if winner == 'x':
                                self.x_score += 1
                                print(f'{winner.upper()}: {self.x_score}')
                            else:
                                self.o_score += 1
                                print(f'{winner.upper()}: {self.o_score}')

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.events()
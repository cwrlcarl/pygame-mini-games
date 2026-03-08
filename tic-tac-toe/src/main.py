import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 700
FPS = 60

PANEL_WIDTH = 500
MARGIN = 50
GRID_TOP = 150
ROWS, COLS = 3, 3
CELL_SIZE = PANEL_WIDTH // COLS
LINE_WIDTH = 5
TEXT_COLOR = (214, 216, 218)
LINE_COLOR = (106, 113, 124)
BG_COLOR = (36, 41, 46)


class TicTacToe:
    def __init__(self):
        pass

    @staticmethod
    def draw_layout(screen):
        for i in range(1, ROWS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN, GRID_TOP + i * CELL_SIZE), (PANEL_WIDTH + MARGIN, GRID_TOP + i * CELL_SIZE), LINE_WIDTH)
        for i in range(1, COLS):
            pygame.draw.line(screen, LINE_COLOR, (MARGIN + i * CELL_SIZE, GRID_TOP), (MARGIN + i * CELL_SIZE, SCREEN_HEIGHT - MARGIN), LINE_WIDTH)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.play = TicTacToe()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.play.draw_layout(self.screen)
        pygame.display.update()

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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
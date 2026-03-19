from settings import *

class TicTacToe:
    def __init__(self):
        self.board = [[None]*3, [None]*3, [None]*3]
        self.turn = 'x'

    def get_board(self):
        return self.board
    
    def get_turn(self):
        return self.turn.upper()
                    
    def handle_click(self, row, col):
        if self.board[row][col] is None:
            if self.turn == 'x':
                self.board[row][col] = 'x'
                self.turn = 'o'
            else:
                self.board[row][col] = 'o'
                self.turn = 'x'
            print(f'Board: {self.board}')

    def check_winner(self):
        for row in range(ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                return self.board[row][0]

        for col in range(COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return self.board[0][col]
        
        return None
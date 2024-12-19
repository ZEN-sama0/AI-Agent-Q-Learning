import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
        return self.board

    def step(self, action, player):
        row, col = action
        if self.board[row, col] != 0:
            raise ValueError("Invalid move!")
        self.board[row, col] = player

        # Check for a winner
        if self.check_winner(player):
            self.done = True
            self.winner = player

        return self.board, self.done

    def check_winner(self, player):
        for row in self.board:
            if np.all(row == player):
                return True
        for col in self.board.T:
            if np.all(col == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

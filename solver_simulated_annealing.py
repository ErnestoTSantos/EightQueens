import math
import random
from solver import QueenSolverBase
from chessboard import ChessBoard


class AnnealingSolver(QueenSolverBase):
    def __init__(self, n=8):
        super().__init__(n)
        self.temp = 1000
        self.cooling = 0.98
        self.min_temp = 0.001

    def _move_queen_randomly(self, board):
        new_positions = list(board.queens)
        col = random.randint(0, self.n - 1)

        new_row = new_positions[col]
        while new_row == new_positions[col]:
            new_row = random.randint(0, self.n - 1)

        new_positions[col] = new_row
        return ChessBoard(n=self.n, queens=new_positions)

    def solve(self):
        board = ChessBoard(n=self.n)
        temp = self.temp
        best = board

        while temp > self.min_temp:
            attacks = board.calculate_attacks()
            if attacks == 0:
                self.solution = board
                return

            new_board = self._move_queen_randomly(board)
            new_attacks = new_board.calculate_attacks()

            diff = new_attacks - attacks

            if diff < 0 or random.random() < math.exp(-diff / temp):
                board = new_board

            if board.calculate_attacks() < best.calculate_attacks():
                best = board

            temp *= self.cooling

        if best.calculate_attacks() == 0:
            self.solution = best
        else:
            self.solution = None

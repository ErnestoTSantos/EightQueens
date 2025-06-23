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

        current_row = new_positions[col]
        new_row = random.randint(0, self.n - 1)

        if self.n > 1:
            while new_row == current_row:
                new_row = random.randint(0, self.n - 1)

        new_positions[col] = new_row
        return ChessBoard(n=self.n, queens=new_positions)

    def solve(self):
        board = ChessBoard(n=self.n)
        temp = self.temp
        best = ChessBoard(n=self.n, queens=list(board.queens))

        print(
            f"Iniciando Simulated Annealing (temp={self.temp}, cooling={self.cooling}, min_temp={self.min_temp})..."
        )

        while temp > self.min_temp:
            current_attacks = board.calculate_attacks()
            if current_attacks == 0:
                print(
                    f"Solução ideal encontrada com 0 ataques antes do resfriamento total!"
                )
                self.solution = board
                return

            new_board = self._move_queen_randomly(board)
            new_attacks = new_board.calculate_attacks()

            diff = new_attacks - current_attacks

            if diff < 0 or random.random() < math.exp(-diff / temp):
                board = new_board

            if board.calculate_attacks() < best.calculate_attacks():
                best = ChessBoard(n=self.n, queens=list(board.queens))

            temp *= self.cooling

        if best.calculate_attacks() == 0:
            self.solution = best
            print(
                f"Busca concluída. Solução ideal encontrada após resfriamento com 0 ataques."
            )
        else:
            self.solution = None
            print(
                f"Busca concluída. Nenhuma solução perfeita encontrada. Melhor estado: {best.queens} com {best.calculate_attacks()} ataques."
            )

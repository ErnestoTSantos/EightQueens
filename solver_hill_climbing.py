from solver import QueenSolverBase
from chessboard import ChessBoard


class HillClimbingSolver(QueenSolverBase):
    def __init__(self, n=8, max_restarts=100):
        super().__init__(n)
        self.max_restarts = max_restarts

    def solve(self):
        for _ in range(self.max_restarts):
            current = ChessBoard(n=self.n)

            while True:
                attacks = current.calculate_attacks()
                if attacks == 0:
                    self.solution = current
                    return

                neighbor, neighbor_attacks = self._best_neighbor(current)

                if neighbor_attacks >= attacks:
                    break

                current = neighbor

    def _best_neighbor(self, board):
        best_board = board
        best_attacks = board.calculate_attacks()

        for col in range(self.n):
            original_row = board.queens[col]
            for row in range(self.n):
                if row == original_row:
                    continue

                new_queens = board.queens[:]
                new_queens[col] = row
                candidate = ChessBoard(n=self.n, queens=new_queens)
                candidate_attacks = candidate.calculate_attacks()

                if candidate_attacks < best_attacks:
                    best_attacks = candidate_attacks
                    best_board = candidate

        return best_board, best_attacks

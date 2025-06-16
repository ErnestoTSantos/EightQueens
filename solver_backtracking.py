from chessboard import ChessBoard


class BacktrackingSolver:
    def __init__(self, n=8):
        self.n = n
        self.solutions = []
        self.solution = None

    def is_safe(self, queens, row, col):
        for c in range(col):
            if queens[c] == row or abs(queens[c] - row) == abs(c - col):
                return False
        return True

    def solve_first(self):
        def backtrack(queens, col):
            if col == self.n:
                self.solution = ChessBoard(n=self.n, queens=queens.copy())
                return True
            for row in range(self.n):
                if self.is_safe(queens, row, col):
                    queens[col] = row
                    if backtrack(queens, col + 1):
                        return True
            return False

        queens = [-1] * self.n
        backtrack(queens, 0)

    def solve_all(self):
        def backtrack(queens, col):
            if col == self.n:
                self.solutions.append(ChessBoard(n=self.n, queens=queens.copy()))
                return
            for row in range(self.n):
                if self.is_safe(queens, row, col):
                    queens[col] = row
                    backtrack(queens, col + 1)

        self.solutions = []
        queens = [-1] * self.n
        backtrack(queens, 0)

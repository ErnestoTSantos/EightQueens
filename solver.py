import time


class QueenSolverBase:
    def __init__(self, n=8):
        self.n = n
        self.solution = None
        self.execution_time = 0

    def solve(self):
        raise NotImplementedError("Implemente o método solve() na subclasse.")

    def run_with_timer(self):
        print(f"Iniciando resolução com {self.__class__.__name__}...")
        start = time.perf_counter()
        self.solve()
        end = time.perf_counter()

        self.execution_time = end - start

        if self.solution:
            print(f"Solução encontrada: {self.solution.queens}")
            print(f"Tempo de execução: {self.execution_time:.4f} segundos")
            if hasattr(self.solution, "plot"):
                self.solution.draw_board()
        else:
            print("Nenhuma solução foi encontrada.")

import random
from chessboard import ChessBoard


class GeneticQueenSolver:
    def __init__(self, n=8, pop_size=100, max_gen=1000, mutation_rate=0.1):
        self.n = n
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.mutation_rate = mutation_rate
        self.target_fitness = (n * (n - 1)) // 2
        self.solution = None

    def create_initial_population(self):
        return [ChessBoard(n=self.n) for _ in range(self.pop_size)]

    def select_parents(self, population):
        scores = [b.get_fitness() for b in population]
        total = sum(scores)
        if total == 0:
            return random.sample(population, 2)

        return random.choices(population, weights=scores, k=2)

    def crossover(self, p1, p2):
        cut = random.randint(1, self.n - 1)
        q1 = p1.queens[:cut] + p2.queens[cut:]
        q2 = p2.queens[:cut] + p1.queens[cut:]
        return ChessBoard(n=self.n, queens=q1), ChessBoard(n=self.n, queens=q2)

    def mutate(self, board):
        if random.random() < self.mutation_rate:
            col = random.randint(0, self.n - 1)
            new_row = random.randint(0, self.n - 1)
            board.queens[col] = new_row
        return board

    def solve(self):
        population = self.create_initial_population()

        for generation in range(self.max_gen):
            for b in population:
                if b.get_fitness() == self.target_fitness:
                    self.solution = b
                    print(f"Solução encontrada na geração {generation}")
                    return

            next_gen = []
            for _ in range(self.pop_size // 2):
                p1, p2 = self.select_parents(population)
                c1, c2 = self.crossover(p1, p2)
                next_gen.append(self.mutate(c1))
                next_gen.append(self.mutate(c2))

            population = next_gen

        print("Solução não encontrada após todas as gerações.")

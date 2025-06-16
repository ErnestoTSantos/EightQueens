import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ChessBoard:
    def __init__(self, n=8, queens=None):
        self.n = n
        if queens:
            if len(queens) != n:
                raise ValueError(f"A lista de rainhas deve ter tamanho {n}")
            self.queens = list(queens)
        else:
            self.queens = [random.randint(0, n - 1) for _ in range(n)]

    def calculate_attacks(self):
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.queens[i] == self.queens[j] or abs(i - j) == abs(
                    self.queens[i] - self.queens[j]
                ):
                    attacks += 1
        return attacks

    def get_fitness(self):
        max_non_attacks = (self.n * (self.n - 1)) // 2
        return max_non_attacks - self.calculate_attacks()

    def plot(self):
        fig, ax = plt.subplots()
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "lightgray"
                ax.add_patch(patches.Rectangle((i, j), 1, 1, facecolor=color))

        for col, row in enumerate(self.queens):
            ax.text(
                col + 0.5,
                row + 0.5,
                "♕",
                fontsize=24,
                ha="center",
                va="center",
                color="black",
            )

        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.n)
        ax.set_xticks(range(self.n + 1))
        ax.set_yticks(range(self.n + 1))
        ax.set_aspect("equal")
        plt.gca().invert_yaxis()
        plt.title(f"Solução para o Problema das {self.n} Rainhas")
        plt.show()

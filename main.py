import time

from solver_genetic import GeneticQueenSolver
from solver_hill_climbing import HillClimbingSolver
from solver_simulated_annealing import AnnealingSolver
from solver_backtracking import BacktrackingSolver


def print_header():
    print("=======================================")
    print(" Resolução dos Problemas das 8 Rainhas ")
    print("=======================================")


def generic_queen():
    solver = GeneticQueenSolver(n=8, pop_size=150, max_gen=2000, mutation_rate=0.15)
    solver.solve()

    if solver.solution:
        print("Tabuleiro final:")
        solver.solution.plot()
    else:
        print("Nenhuma solução foi encontrada.")


def hill_climbing_queen():
    hc_solver = HillClimbingSolver(max_restarts=200)
    hc_solver.run_with_timer()


def simulated_annealing_queen():
    print("Rodando o algoritmo de recozimento simulado (com paciência)...")
    solver = AnnealingSolver(n=8)
    start = time.time()
    solver.solve()
    end = time.time()

    if solver.solution:
        print("Solução encontrada!")
        print(f"Tabuleiro: {solver.solution.queens}")
        print(f"Ataques restantes: {solver.solution.calculate_attacks()}")
    else:
        print("Não foi dessa vez. Tente rodar de novo, talvez com mais sorte.")

    print(f"Tempo gasto: {end - start:.2f} segundos")


def backtracking():
    print("Buscando primeira solução com backtracking...")
    solver = BacktrackingSolver()
    solver.solve_first()
    if solver.solution:
        solver.solution.plot()
    else:
        print("Nenhuma solução encontrada.")

    print("\n--- Buscando todas as soluções ---")
    full_solver = BacktrackingSolver()
    start = time.perf_counter()
    full_solver.solve_all()
    duration = time.perf_counter() - start

    print(f"Total de soluções: {len(full_solver.solutions)}")
    print(f"Tempo de execução: {duration:.4f} segundos")


def main():
    print_header()
    print("Escolha o algoritmo para resolver o problema das 8 rainhas:")
    print("1. Algoritmo Genético")
    print("2. Hill Climbing")
    print("3. Simulated Annealing")
    print("4. Backtracking")

    choice = input("Digite o número da opção desejada: ")

    if choice == "1":
        generic_queen()
    elif choice == "2":
        hill_climbing_queen()
    elif choice == "3":
        simulated_annealing_queen()
    elif choice == "4":
        backtracking()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


main()

#### Genetic Algorithm

from utils.utils import tour_cost,swap_neighbor
import random
from utils.utils import select_solution_from_pool


def selection(population, matrix, k=3):

    candidates = random.sample(population, k)

    best = min(candidates, key=lambda sol: tour_cost(sol, matrix))

    return best
def crossover(parent1, parent2):

    n = len(parent1)

    start, end = sorted(random.sample(range(n), 2))

    child = [-1] * n

    # segment parent1
    child[start:end] = parent1[start:end]

    remaining = [c for c in parent2 if c not in child]

    j = 0
    for i in range(n):

        if child[i] == -1:
            child[i] = remaining[j]
            j += 1

    return child

def mutation(solution, rate=0.1):

    n = len(solution)

    if random.random() < rate:

        i, j = random.sample(range(n), 2)

        solution[i], solution[j] = solution[j], solution[i]

    return solution


def run_ga(matrix, elite_pool, iterations=200):

    n = len(matrix)
    population_size = 50

    # population initiale
    population = []
    for _ in range(population_size):

        sol = list(range(n))
        random.shuffle(sol)

        population.append(sol)

    for iteration in range(iterations):

        new_population = []

        for _ in range(population_size):

            # sélection
            parent1 = selection(population, matrix)
            parent2 = selection(population, matrix)

            # crossover
            child = crossover(parent1, parent2)

            # mutation
            child = mutation(child)

            new_population.append(child)

            cost = tour_cost(child, matrix)

            # ajouter au pool
            elite_pool.append((child, cost, "GA"))

        # nouvelle génération
        population = new_population

        # limiter elite pool
        if len(elite_pool) > 20:
            elite_pool[:] = sorted(elite_pool, key=lambda x: x[1])[:20]

        # migration périodique
        if iteration % 50 == 0:

            candidate = select_solution_from_pool(elite_pool)

            if candidate is not None:

                # remplacer le pire individu
                worst_index = max(
                    range(len(population)),
                    key=lambda i: tour_cost(population[i], matrix)
                )

                population[worst_index] = candidate

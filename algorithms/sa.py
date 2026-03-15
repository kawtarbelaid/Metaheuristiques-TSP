#### Simulated Annealing

from utils.utils import tour_cost,swap_neighbor
import random
import math 
from utils.utils import select_solution_from_pool
from utils.utils import two_opt_swap
from algorithms.glouton import glouton_tsp


def run_sa(matrix, elite_pool,startGreedy, iterations=5000):

    n = len(matrix)

    # Cold Start 
    # solution = list(range(n))
    # random.shuffle(solution)

    # # Warm start
    solution = glouton_tsp(matrix,startGreedy)[0] 

    cost = tour_cost(solution, matrix)

    # paramètres SA
    T = 5000
    cooling_rate = 0.999

    for iteration in range(iterations):

        # choisir deux positions
        i, j = sorted(random.sample(range(n), 2))

        # voisinage 2-opt
        new_solution = two_opt_swap(solution, i, j)

        new_cost = tour_cost(new_solution, matrix)

        delta = new_cost - cost

        # règle SA
        if delta < 0:

            solution = new_solution
            cost = new_cost

        else:

            prob = math.exp(-delta / T)

            if random.random() < prob:

                solution = new_solution
                cost = new_cost

        # refroidissement
        T *= cooling_rate

        # ajouter au pool
        elite_pool.append((solution, cost, "SA"))

        # limiter elite pool
        if len(elite_pool) > 20:

            elite_pool[:] = sorted(elite_pool, key=lambda x: x[1])[:20]

        # migration périodique
        if iteration % 200 == 0:

            candidate = select_solution_from_pool(elite_pool)

            if candidate is not None:

                solution = candidate
                cost = tour_cost(solution, matrix)
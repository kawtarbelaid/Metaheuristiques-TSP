#### Threshold Accepting

from utils.utils import tour_cost,swap_neighbor
import random
from utils.utils import select_solution_from_pool
from algorithms.glouton import glouton_tsp



def threshold_accepting(matrix, shared_pool, max_iter=1000):
    print("TA started")
    n = len(matrix)
    current = list(range(n))
    random.shuffle(current)
    current_cost = tour_cost(current, matrix)

    threshold = 100
    decay = 0.99

    for iteration in range(max_iter):

        neighbor = swap_neighbor(current)
        neighbor_cost = tour_cost(neighbor, matrix)

        if neighbor_cost - current_cost < threshold:
            current = neighbor
            current_cost = neighbor_cost

        threshold *= decay

        if iteration % 200 == 0:
            shared_pool.append(("TA",current, current_cost))


def run_ta(matrix, elite_pool,startGreedy, threshold=50, iterations=2000):

    n = len(matrix)

    # -------------Cold Start-------------
    # solution = list(range(n))
    # random.shuffle(solution)

    # -------------Warm Start-------------
    solution = glouton_tsp(matrix,startGreedy)[0] 

    cost = tour_cost(solution, matrix)

    for _ in range(iterations):

        i, j = random.sample(range(n), 2)

        new_solution = solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        new_cost = tour_cost(new_solution, matrix)

        if new_cost - cost < threshold:

            solution = new_solution
            cost = new_cost

        elite_pool.append((solution, cost, "TA"))

        # limiter elite pool
        if len(elite_pool) > 20:
            elite_pool[:] = sorted(elite_pool, key=lambda x: x[1])[:20]


        if _ % 200 == 0:

            candidate = select_solution_from_pool(elite_pool)

            if candidate is not None:
                solution = candidate

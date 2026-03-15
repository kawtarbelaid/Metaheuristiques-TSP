from utils.utils import tour_cost
import time

def glouton_tsp(distance_matrix, start=1):
    start_time = time.perf_counter()   # début du chronométrage

    n = len(distance_matrix)

    villes = list(range(1, n + 1))
    tour = [start]
    non_visitees = set(villes)
    non_visitees.remove(start)

    ville_courante = start

    while non_visitees:
        prochaine_ville = min(
            non_visitees,
            key=lambda v: distance_matrix[ville_courante - 1][v - 1]
        )

        tour.append(prochaine_ville)
        non_visitees.remove(prochaine_ville)
        ville_courante = prochaine_ville

    end_time = time.perf_counter()   # fin du chronométrage

    execution_time = end_time - start_time

    return tour, execution_time

# --------------Meilleure tourné glouton avec changement de ville de départ--------------
def best_glouton(matrix):
    start_time = time.perf_counter()   # début du chronométrage
    
    n = len(matrix)

    best_cost = float('inf')
    best_tour = None

    for start in range(1, n+1):

        tour, temps = glouton_tsp(matrix, start=start)
        cost = tour_cost(tour, matrix)

        if cost < best_cost:
            best_cost = cost
            best_tour = tour
            best_time = temps
            best_start = start

    return best_start, best_cost, best_time


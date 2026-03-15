import random
import math
import time
import os
from multiprocessing import Process, Manager


# --------- GET DISTANCES MATRIX ---------
def lire_matrice_txt(fichier):
    matrice = []
    
    with open(fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                valeurs = list(map(float, ligne.split()))
                matrice.append(valeurs)
    
    return matrice

def parcourir_TSPLIB(input_folder):
    instances = {}
    
    for filename in os.listdir(input_folder):

        if filename.endswith(".txt"):
            output = filename.replace(".txt", "")
            
            chemin_complet = os.path.join(input_folder, filename)

            instances[output] = lire_matrice_txt(chemin_complet)

    return instances


def tour_cost(tour, matrix):
    cost = 0

    for i in range(len(tour)-1):
        cost += matrix[tour[i]-1][tour[i+1]-1]

    cost += matrix[tour[-1]-1][tour[0]-1]

    return cost


# --------- NEIGHBOR (swap) ---------

def swap_neighbor(tour):
    i, j = random.sample(range(len(tour)), 2)
    new_tour = tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour


# --------- Selection aléatoire des solutions du Pool---------
def select_solution_from_pool(elite_pool):

    if len(elite_pool) == 0:
        return None

    r = random.random()

    pool_list = list(elite_pool)

    # 70% exploitation
    if r < 0.7:

        best = min(pool_list, key=lambda x: x[1])
        return best[0]

    # 30% exploration
    else:

        candidate = random.choice(pool_list)
        return candidate[0]
    

# --------- Fonction 2-opt ---------
def two_opt_swap(route, i, j):

    new_route = route[:]

    new_route[i:j+1] = reversed(route[i:j+1])

    return new_route
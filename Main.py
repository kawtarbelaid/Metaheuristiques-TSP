from core.cooperative_solver import cooperative_run
from utils.utils import parcourir_TSPLIB
from utils.utils import tour_cost
import os
from algorithms.glouton import glouton_tsp
from algorithms.glouton import best_glouton
def main():

    instances = parcourir_TSPLIB("data/matrices")

    print("\n===== Projet Métaheuristiques TSP =====")

    while True:

        print("\nMenu :")
        print("1 - Exécuter l'algorithme glouton")
        print("2 - Exécuter la métaheuristique coopérative")
        print("3 - Comparer Glouton vs Métaheuristique")
        print("4 - Quitter")

        choix = input("Votre choix : ")

        if choix == "4":
            print("Fin du programme.")
            break

        # afficher les instances disponibles
        print("\nInstances disponibles :")

        names = list(instances.keys())
        for i, name in enumerate(names):
            print(f"{i} - {name}")

        index = int(input("Choisir une instance : "))
        matrice = instances[names[index]]

        #Best start ville glouton pour chaque instance respectivement
        Best_start =[10,40,117,4,71,29,8,53,85,15,28]
        startM = Best_start[index]
    # ---------------- GLUTTON ----------------

        if choix == "1":

            start = int(input("Ville de départ : "))

            tour, temps = glouton_tsp(matrice, start)

            cost = tour_cost(tour, matrice)

            print("\nRésultat Glouton")
            print("Coût :", cost)
            print("Temps :", temps)

        # ---------------- METAHEURISTIQUE ----------------

        elif choix == "2":
            solution, cost, algo, temps = cooperative_run(matrice,startM)

            print("\nRésultat Métaheuristique")
            print("Algorithme :", algo)
            print("Coût :", cost)
            print("Temps :", temps)

        # ---------------- COMPARAISON ----------------

        elif choix == "3":

            print("\nCalcul glouton...")

            best_start, best_cost, best_time = best_glouton(matrice)

            print("Glouton :")
            print("Start :", best_start)
            print("Cost :", best_cost)
            print("Temps :", best_time)

            print("\nCalcul métaheuristique...")

            solution, cost, algo, temps = cooperative_run(matrice,startM)

            print("Metaheuristique :")
            print("Algorithme :", algo)
            print("Cost :", cost)
            print("Temps :", temps)

            gain = 100 * (best_cost - cost) / best_cost

            print("Gain (%) :", gain)

        else:
            print("Choix invalide")


    
if __name__ == "__main__":
    main()
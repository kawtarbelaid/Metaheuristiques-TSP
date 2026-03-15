from algorithms.ga import run_ga
from algorithms.sa import run_sa
from algorithms.ta import run_ta
from multiprocessing import Process, Manager
import time


def cooperative_run(matrix,startt):

    manager = Manager()

    elite_pool = manager.list()

    start = time.time()

    p1 = Process(target=run_ga, args=(matrix, elite_pool))
    p2 = Process(target=run_sa, args=(matrix, elite_pool,startt))
    p3 = Process(target=run_ta, args=(matrix, elite_pool,startt))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.time()

    best = min(elite_pool, key=lambda x: x[1])

    # print("Best cost :", best[1])
    # print("Found by :", best[2])
    # print("Execution time :", end-start)
    return best[0], best[1], best[2],end-start
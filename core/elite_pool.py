import random

class ElitePool:

    def __init__(self, max_size=10):
        self.pool = []
        self.max_size = max_size

    def add_solution(self, solution, cost, source):

        self.pool.append((solution, cost, source))

        # trier par coût
        self.pool.sort(key=lambda x: x[1])

        # garder seulement les meilleures
        if len(self.pool) > self.max_size:
            self.pool = self.pool[:self.max_size]

    def get_random_solution(self):

        if len(self.pool) == 0:
            return None

        return random.choice(self.pool)

    def get_best(self):

        if len(self.pool) == 0:
            return None

        return min(self.pool, key=lambda x: x[1])
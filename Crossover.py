import numpy as np
import random


class Crossover:
    @staticmethod
    def binomial_crossover(mutated, parent, cr, dims):
        trial_vectors = [[0]*len(mutated[0]) for i in range(len(mutated))]
        prob = np.random.uniform(2, (0, 1))
        for i in range(len(mutated)):
            for j in range(dims):
                if prob[j] <= cr:
                    trial_vectors[i][j] = mutated[i][j]
                else:
                    trial_vectors[i][j] = parent[i][j]
        return trial_vectors

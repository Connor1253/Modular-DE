import random
import numpy as np

class Initialisation:

    # Creates a 2d array between a given set of bounds

    @staticmethod
    def initialise(bounds, Np, dims):
        x = [[0] * dims for i in range(Np)]
        # Np = number of solutions generated
        # dims = amount of numbers in each solution
        for i in range(Np):
            for j in range(dims):
                x[i][j] = random.randint(bounds[0], bounds[1])
        return x

    @staticmethod
    def latin_hypercube(bounds, data_points, dims):
        pairs = [[0] * dims for i in range(data_points)]
        for i in range(dims):
            LB = bounds[0]
            UB = bounds[1]
            const = 2
            for j in range(data_points):
                pairs[j][i] = np.round(np.random.uniform(LB, UB / data_points), 0)
                LB = UB / data_points
                UB = bounds[1] * const
                const += 1
        return pairs




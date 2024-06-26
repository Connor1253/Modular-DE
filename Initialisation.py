import random


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





import numpy as np


class Mutation:
    @staticmethod
    def compute(x):
        v_x = [i[0] for i in x]
        v_y = [i[1] for i in x]
        return [v_x, v_y]

    @staticmethod
    def candidates_n(x, i, n):
        randSols = []
        index_list = []
        while len(index_list) < n:
            rand_index = np.random.randint(0, len(x) - 1)
            if rand_index != i and rand_index not in index_list:
                index_list.append(rand_index)
                randSols.append(x[rand_index])
        return np.asarray(randSols)

    @staticmethod
    def rand_1(init, F, best):
        v = [[0]*len(init[0]) for i in range(len(init))]
        for i in range(len(init)):
            candidates = Mutation.candidates_n(init, i, 3)
            thing = Mutation.compute(candidates)
            for j in range(len(thing[0])-1):
                v[i][j] = thing[j][0] + F * (thing[j][1] - thing[j][2])
        return v

    @staticmethod
    def best_1(init, F, best):
        v = [[0]*len(init[0]) for i in range(len(init))]
        for i in range(len(init)):
            candidates = Mutation.candidates_n(init, i, 2)
            thing = Mutation.compute(candidates)
            for j in range(len(thing[0])):
                v[i][j] = best[j] + F * (thing[j][0] - thing[j][1])
        return v

    @staticmethod
    def rand_2(init, F, best):
        v = [[0] * len(init[0]) for i in range(len(init))]
        for i in range(len(init)):
            candidates = Mutation.candidates_n(init, i, 5)
            thing = Mutation.compute(candidates)
            for j in range(len(thing)):
                v[i][j] = thing[j][0] + F * (thing[j][1] - thing[j][2]) + F * (thing[j][3] - thing[j][4])
        return v

    @staticmethod
    def best_2(init, F, best):
        v = [[0] * len(init[0]) for i in range(len(init))]
        for i in range(len(init)):
            candidates = Mutation.candidates_n(init, i, 4)
            thing = Mutation.compute(candidates)
            for j in range(len(best)):
                v[i][j] = best[j] + F * (thing[j][0] - thing[j][1]) + F * (thing[j][2] - thing[j][3])
        return v
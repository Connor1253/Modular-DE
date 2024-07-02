import random


class jDE:
    @staticmethod
    def generate_F():
        return random.uniform(0, 1)

    @staticmethod
    def generate_CR():
        return random.uniform(0, 1)

    @staticmethod
    def update_F(curr_F, FL = 0.1, FU = 0.9, T1 = 0.1):
        rand_1 = jDE.generate_F()
        rand_2 = jDE.generate_F()
        if(rand_2 < T1):
            return FL + rand_1 * FU
        else:
            return curr_F

    @staticmethod
    def update_CR(curr_CR, T2 = 0.1):
        rand_3 = jDE.generate_CR()
        rand_4 = jDE.generate_CR()
        if(rand_4 < T2):
            return rand_3
        else:
            return curr_CR
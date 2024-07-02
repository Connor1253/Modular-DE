from Initialisation import Initialisation as init
from Mutation import Mutation
from Crossover import Crossover
from Selection import Selection
from jDE import jDE
import numpy as np

@staticmethod
def sphere(x):
    return (x[0]) ** 2 + (x[1]) ** 2

class DE:
    @staticmethod
    def DE(iters, NP=30, bounds=[0, 100], F=0.5, cr=0.5,
           objFunc=[sphere],
           initialisation=init.initialise,
           mutator= Mutation.best_1,
           crossover=Crossover.binomial_crossover,
           updateCR=jDE.update_CR,
           updateF=jDE.update_F):

        for j in range(len(objFunc)):
            x = initialisation(bounds, NP, 2)
            for i in range(iters):
                best_value = np.min([objFunc[j](i) for i in x])
                best_arr = x[np.argmin([objFunc[j](i) for i in x])]
                mutated = mutator(x, F, best_arr)
                if crossover is None:
                    trialVector = mutated
                else:
                    trialVector = crossover(mutated, x, cr, 2)
                x = Selection.greedy_selection(x, NP, trialVector, objFunc[j])
            cr = updateCR(cr)
            F = updateF(F)
        formated_best_arr = [ "{:0.2f}".format(x) for x in best_arr]
        return '{:.2f}'.format(best_value), formated_best_arr

print(DE.DE(1000))






class Selection:

    @staticmethod
    def greedy_selection(init, np, trial_vectors, objective):
        len_trial = len(trial_vectors)
        init = [*init, *trial_vectors]
        # Sorts based on objective function
        init = sorted(init, key=objective)
        return init[:np]
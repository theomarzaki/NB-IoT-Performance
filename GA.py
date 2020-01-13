# This file handles the architecture of the GA component

# 1) Initial Population
# 2) Fitness function
# 3) Selection
# 4) Cross-Over
# 5) Mutation
# 6) Termination --> when the population has converged. parents ~ children


class GA():

    def __init__(self):
        pass

    def initial_population(self):
        #individual configurations for sol
        pass

    def apply_fitness(self,population):
        # determines the 'score' of the configurations
        pass

    def selection(self,population):
        # selection of the fittest individual for 'reproduction'
        pass

    def cross_over(self,population):
        # cross-over ('slice') point for the pair of parents chosen
        pass

    def mutate(self,population):
        # low probability, allows exploration of state space
        pass

    def converged(self):
        # boolean value to check whether the children and the parents are the same
        return False

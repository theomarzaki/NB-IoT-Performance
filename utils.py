from GA import GA
from logging import log

# START
# Generate the initial population
# Compute fitness
# REPEAT
#     Selection
#     Crossover
#     Mutation
#     Compute fitness
# UNTIL population has converged
# STOP

def Evolve():
    # 'training/exploration' for the GA. Computing optimal Configration
    GA_wrapper = GA()
    population = GA_wrapper.initial_population()
    fitness = GA_wrapper.apply_fitness(population)
    best_fitness, best_config = GA_wrapper.get_best_config(population)
    while(True):
        log.debug("Selecting Population ... ")
        selected_population = GA_wrapper.selection(population)
        log.debug("Applying Cross-Over ...")
        crossed_population = GA_wrapper.cross_over(selected_population)
        log.debug("Mutating Population ...")
        mutated_population = GA_wrapper.mutate(crossed_population)

        new_fitness,new_config = GA_wrapper.get_best_config(mutated_population)

        if new_fitness > best_fitness:
            best_fitness = new_fitness
            best_config = new_config

        log.debug("Current Best Fitness: {}, Best Fitness: {}, Config: {}".format(best_fitness,new_fitness,new_config))

        if(GA_wrapper.converged()):
            log.debug("Evolution Converged ... Best Fitness: {}, Config: {}".format(best_fitness,best_config))
            break

    return best_config

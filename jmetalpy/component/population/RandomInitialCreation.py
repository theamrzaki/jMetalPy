import threading

from jmetalpy.component.population import PopulationArk
from jmetalpy.core.algorithm.observable import DefaultObservable
from jmetalpy.core.problem import Problem


class RandomInitialCreation(DefaultObservable, threading.Thread):

    def __init__(self, population_size: int):
        super(RandomInitialCreation, self).__init__()
        self.population_size = population_size

    def apply(self, problem: Problem):
        population = PopulationArk(population_size=self.population_size)

        for _ in range(0, self.population_size):
            individual = problem.create_solution()
            population.add(individual)

        population.__setattr__("evaluations", 0)
        population.__setattr__("mating_pool", None)
        population.__setattr__("is_terminated", False)
        population.__setattr__("problem", problem)

        observable_data = {'population': population}
        self.notify_all(**observable_data)

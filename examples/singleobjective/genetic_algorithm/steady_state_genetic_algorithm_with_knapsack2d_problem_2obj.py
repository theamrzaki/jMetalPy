import sys
import numpy as np
sys.path.append("C:\PhD Research\Test\jMetalPy\jmetal")

from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection, BitFlipMutation, SPXCrossover
from problem.singleobjective.Knapsack2d_2objs import Knapsack2d_2objs
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == "__main__":
    problem = Knapsack2d_2objs(
        number_of_users = 3,
        number_of_workers = 4,
        profits = [[1,5,2,1],
                   [1,5,3,1],
                   [0,0,0,0]],
        mask = [[1,1,1,1],
                [1,1,1,1],
                [-np.inf,-np.inf,-np.inf,-np.inf]],
    )

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=100,
        offspring_population_size=1,
        mutation=BitFlipMutation(probability=0.1),
        crossover=SPXCrossover(probability=0.8),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=10000),
    )

    algorithm.run()
    subset = algorithm.get_result()

    print("Algorithm: {}".format(algorithm.get_name()))
    print("Problem: {}".format(problem.get_name()))
    print("Solution: {}".format(subset.variables))
    print("Fitness: {}".format(-subset.objectives[0]))
    print("Computing time: {}".format(algorithm.total_computing_time))
    print(f"Problem Maximum Capacity: {problem.capacity}")

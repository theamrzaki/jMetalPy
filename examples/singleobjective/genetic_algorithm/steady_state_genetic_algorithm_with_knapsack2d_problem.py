import os
import sys
sys.path.append("C:\PhD Research\Test\jMetalPy\jmetal")

from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection, BitFlipMutation, SPXCrossover
from problem.singleobjective.Knapsack2d import Knapsack2d
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == "__main__":
    problem = Knapsack2d(
        number_of_users = 2,
        number_of_workers = 4,
        profits = [[1,2,1,1],
                   [1,1,2,1]]
    )

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=100,
        offspring_population_size=1,
        mutation=BitFlipMutation(probability=0.1),
        crossover=SPXCrossover(probability=0.8),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=400),
    )

    algorithm.run()
    subset = algorithm.get_result()

    print("Algorithm: {}".format(algorithm.get_name()))
    print("Problem: {}".format(problem.get_name()))
    print("Solution: {}".format(subset.variables))
    print("Fitness: {}".format(-subset.objectives[0]))
    print("Computing time: {}".format(algorithm.total_computing_time))
    print(f"Problem Maximum Capacity: {problem.capacity}")

import os
import sys
sys.path.append("C:\PhD Research\Test\jMetalPy\jmetal")

from problem.multiobjective.Knapsack2d import Knapsack2d
from jmetal.algorithm.multiobjective.mocell import MOCell
from jmetal.operator import PolynomialMutation, SBXCrossover
from jmetal.problem import ZDT1, ZDT4
from jmetal.util.archive import CrowdingDistanceArchive
from jmetal.util.neighborhood import C9
from jmetal.util.solution import (
    print_function_values_to_file,
    print_variables_to_file,
    read_solutions,
)
from jmetal.util.termination_criterion import StoppingByEvaluations


if __name__ == "__main__":
    from problem.multiobjective.Knapsack2d import Knapsack2d

    problem = Knapsack2d(
        number_of_users = 2,
        number_of_workers = 4,
        profits = [[1,2,1,1],
                   [1,1,2,1]]
    )

    max_evaluations = 1000

    algorithm = MOCell(
        problem=problem,
        population_size=100,
        neighborhood=C9(10, 10),
        archive=CrowdingDistanceArchive(100),
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    algorithm.run()
    subset = algorithm.get_result()

    print("Algorithm: {}".format(algorithm.get_name()))
    print("Problem: {}".format(problem.get_name()))
    print("Solution: {}".format(subset.variables))
    print("Fitness: {}".format(-subset.objectives[0]))
    print("Fitness: {}".format(-subset.objectives[1]))
    print("Computing time: {}".format(algorithm.total_computing_time))
    print(f"Problem Maximum Capacity: {problem.capacity}")

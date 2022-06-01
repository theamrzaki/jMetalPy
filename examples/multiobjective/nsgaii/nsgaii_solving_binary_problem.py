from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import BitFlipMutation, SPXCrossover
from jmetal.problem.multiobjective.unconstrained import OneZeroMax
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.operator import BinaryTournamentSelection, BitFlipMutation, SPXCrossover

"""  
Program to  configure and run the NSGA-II algorithm configured to solve a binary problem, OneZeroMax, which is 
multiobjective version of the ONE_MAX problem where the numbers of 1s and 0s have to be maximized at the same time.
"""

if __name__ == "__main__":
    binary_string_length = 512
    #problem = OneZeroMax(binary_string_length)

    import sys
    sys.path.append("C:\PhD Research\Test\jMetalPy\jmetal")
    from problem.multiobjective.Knapsack2d import Knapsack2d
    problem = Knapsack2d(
        number_of_users = 10,
        number_of_workers = 4,
        profits = [[1,2,1,1],
                   [1,1,2,1],
                   [1,1,2,1],
                   [1,1,2,1],
                   [1,1,2,1],
                   [1,2,1,1],
                   [1,1,2,1],
                   [1,1,2,1],
                   [1,1,2,1],
                   [1,1,2,1]]
    )
    
    max_evaluations = 10000
    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=BitFlipMutation(probability=0.1),
        crossover=SPXCrossover(probability=0.8),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    algorithm.run()
    front = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(front, "FUN." + algorithm.label)
    print_variables_to_file(front, "VAR." + algorithm.label)

    print(f"Algorithm: {algorithm.get_name()}")
    print(f"Problem: {problem.get_name()}")
    print(f"Computing time: {algorithm.total_computing_time}")

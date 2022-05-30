import random

import numpy as np

from jmetal.core.problem import BinaryProblem
from jmetal.core.solution import BinarySolution

"""
.. module:: knapsack
   :platform: Unix, Windows
   :synopsis: Single Objective Knapsack problem

.. moduleauthor:: Alejandro Marrero <alu0100825008@ull.edu.es>
"""


class Knapsack2d(BinaryProblem):
    """Class representing Knapsack with 2 dimention (multiple users) Problem."""

    def __init__(
        self,
        number_of_users: int = 2,
        number_of_workers: int = 4,
        capacity: float = 1000,
        weights: list = None,
        profits: list = None,
        from_file: bool = False,
        filename: str = None,
    ):
        super(Knapsack2d, self).__init__()

        if from_file:
            self.__read_from_file(filename)
        else:
            self.capacity = capacity
            self.weights = weights
            self.profits = profits
            self.number_of_bits = number_of_workers

        self.number_of_variables = number_of_users
        self.obj_directions = [self.MAXIMIZE]
        self.number_of_objectives = 1
        self.number_of_constraints = 1

    def evaluate(self, solution: BinarySolution) -> BinarySolution:
        total_profits = 0.0
        #total_weigths = 0.0

        for user,v in enumerate(solution.variables):
            for index, bits in enumerate(v):
                if bits:
                    total_profits += self.profits[user][index]
                    #total_weigths += self.weights[index]

        for v in solution.variables:
            if sum(v) > 1:
                total_profits = 0.0

        solution.objectives[0] = -1.0 * total_profits
        return solution

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(
            number_of_variables=self.number_of_variables, number_of_objectives=self.number_of_objectives
        )

        for i,_ in enumerate(new_solution.variables):
            new_solution.variables[i] = [True if random.randint(0, 1) == 0 else False for _ in range(self.number_of_bits)]

        return new_solution

    def get_name(self):
        return "Knapsack"

import random

from jmetalpy.core.operator import Mutation
from jmetalpy.core.solution import BinarySolution


class BitFlip(Mutation[BinarySolution]):
    def __init__(self, probability: float):
        super(BitFlip, self).__init__(probability=probability)

    def execute(self, solution: BinarySolution) -> BinarySolution:
        for i in range(solution.number_of_variables):
            for j in range(len(solution.variables[i])):
                rand = random.random()
                if rand <= self.probability:
                    solution.variables[i][j] = True if solution.variables[i][j] == False else False

        return solution

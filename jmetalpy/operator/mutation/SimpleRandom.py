import random

from jmetalpy.core.operator import Mutation
from jmetalpy.core.solution import FloatSolution


class SimpleRandom(Mutation):
    def __init__(self, probability: float):
        super(SimpleRandom, self).__init__(probability=probability)

    def get_name(self):
        return "Simple random mutation"

    def execute(self, solution: FloatSolution) -> FloatSolution:
        for i in range(solution.number_of_variables):
            rand = random.random()
            if rand <= self.probability:
                solution.variables[i] = solution.lower_bound[i] + \
                                        (solution.upper_bound[i] - solution.lower_bound[i]) * random.random()
        return solution


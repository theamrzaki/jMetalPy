import random

from jmetalpy.core.operator import Mutation
from jmetalpy.core.solution import FloatSolution


class Uniform(Mutation):

    def __init__(self, probability: float, perturbation: float = 0.5):
        super(Uniform, self).__init__(probability=probability)
        self.perturbation = perturbation

    def get_name(self):
        return "Uniform mutation"

    def execute(self, solution: FloatSolution) -> FloatSolution:
        for i in range(solution.number_of_variables):
            rand = random.random()

            if rand <= self.probability:
                tmp = (random.random() - 0.5) * self.perturbation
                tmp += solution.variables[i]

                if tmp < solution.lower_bound[i]:
                    tmp = solution.lower_bound[i]
                elif tmp > solution.upper_bound[i]:
                    tmp = solution.upper_bound[i]

                solution.variables[i] = tmp

        return solution

from queue import Queue
import logging
import random

from jmetalpy.core.operator import Mutation
from jmetalpy.core.population import Population
from jmetalpy.core.solution import FloatSolution

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Polynomial(Mutation):
    def __init__(self, probability: float, distribution_index: float = 0.20):
        super(Polynomial, self).__init__(probability=probability)
        self.buffer = Queue()
        self.distribution_index = distribution_index

    def update(self, *args, **kwargs):
        logger.info("MUTATION update invoked")
        population = kwargs['POPULATION']

        try:
            self.buffer.put(population)
        except Exception as ex:
            print("MUTATION: " + str(ex))

    def execute(self, solution: FloatSolution) -> FloatSolution:
        for i in range(solution.number_of_variables):
            rand = random.random()

            if rand <= self.probability:
                y = solution.variables[i]
                yl, yu = solution.lower_bound[i], solution.upper_bound[i]

                if yl == yu:
                    y = yl
                else:
                    delta1 = (y - yl) / (yu - yl)
                    delta2 = (yu - y) / (yu - yl)
                    rnd = random.random()
                    mut_pow = 1.0 / (self.distribution_index + 1.0)
                    if rnd <= 0.5:
                        xy = 1.0 - delta1
                        val = 2.0 * rnd + (1.0 - 2.0 * rnd) * (pow(xy, self.distribution_index + 1.0))
                        deltaq = pow(val, mut_pow) - 1.0
                    else:
                        xy = 1.0 - delta2
                        val = 2.0 * (1.0 - rnd) + 2.0 * (rnd - 0.5) * (pow(xy, self.distribution_index + 1.0));
                        deltaq = 1.0 - pow(val, mut_pow)

                    y += deltaq * (yu - yl)
                    if y < solution.lower_bound[i]:
                        y = solution.lower_bound[i]
                    if y > solution.upper_bound[i]:
                        y = solution.upper_bound[i]

                solution.variables[i] = y

        return solution

    def apply(self, population: Population):
        if not population.is_terminated:
            logger.info("MUTATION: APPLY invoked")
            pass

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

    def run(self):
        logger.info("MUTATION: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("MUTATION: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            print("MUTATION: " + str(ex))

        logger.info("MUTATION: END RUN")

    def get_name(self):
        return "Polynomial mutation"

import logging
from queue import Queue

from jmetalpy.core.algorithm.observable import DefaultObservable
from jmetalpy.core.population import Population
from jmetalpy.core.problem import Problem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RandomInitialPopulation(DefaultObservable):

    def __init__(self, population_size: int):
        super(RandomInitialPopulation, self).__init__()
        self.buffer = Queue()
        self.population_size = population_size

    def apply(self, problem: Problem):
        logger.info("RANDOM_POPULATION_CREATION: Apply invoked")
        population = Population()

        for _ in range(0, self.population_size):
            population.append(problem.create_solution())

        population.evaluations = 0
        population.mating_pool = None
        population.is_terminated = False
        population.problem = problem

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

        self.buffer.put(True)

    def run(self):
        logger.info("RANDOM POPULATION CREATOR OBSERVER: RUN")

        try:
            self.buffer.get()
        except Exception as ex:
            print("RANDOM POPULATION ex: " + str(ex))

        logger.info("RANDOM POPULATION CREATOR OBSERVER: END RUN")

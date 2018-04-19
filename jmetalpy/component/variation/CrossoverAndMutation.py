import logging
from queue import Queue

from jmetalpy.core.operator import Crossover, Mutation

from jmetalpy.core.operator import Operator
from jmetalpy.core.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CrossoverAndMutation(Operator):

    def __init__(self, crossover: Crossover, mutation: Mutation, offspring_population_size: int):
        super(CrossoverAndMutation, self).__init__()
        self.buffer = Queue()
        self.crossover_operator = crossover
        self.mutation_operator = mutation
        self.offspring_population_size = offspring_population_size

    def update(self, *args, **kwargs):
        logger.info("VARIATION update invoked")
        population = kwargs["POPULATION"]

        try:
            self.buffer.put(population)
        except Exception as ex:
            raise Exception("VARIATION buffer ex: " + str(ex))

    def apply(self, population: Population):
        if not population.is_terminated:
            logger.info("VARIATION: APPLY invoked")

            number_of_parents_to_combine = self.crossover_operator.get_number_of_parents()
            self.__check_number_of_parents(population, number_of_parents_to_combine)

            offspring_population = []
            for i in range(0, len(population), number_of_parents_to_combine):
                parents = []
                for j in range(number_of_parents_to_combine):
                    parents.append(population[i + j])

                offspring = self.crossover_operator.execute(parents)

                for solution in offspring:
                    self.mutation_operator.execute(solution)
                    offspring_population.append(solution)

                    if len(offspring_population) >= self.offspring_population_size:
                        break

            population.mating_pool = offspring_population

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

    def __check_number_of_parents(self, population: Population, number_of_parents_for_crossover: int):
        if len(population) % number_of_parents_for_crossover != 0:
            raise Exception("Wrong number of parents: the remainder of the population size ({0}) is not "
                            "divisible by {1}".format(len(population), number_of_parents_for_crossover))

    def run(self):
        logger.info("VARIATION OBSERVER: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("VARIATION OBSERVER: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            raise Exception("VARIATION ex: " + str(ex))

        logger.info("VARIATION OBSERVER: END RUN")

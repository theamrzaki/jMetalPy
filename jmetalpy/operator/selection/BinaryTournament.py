import logging
from queue import Queue
import random
from copy import copy
from typing import TypeVar

from jmetalpy.core.operator import Selection
from jmetalpy.core.comparator import Comparator
from jmetalpy.component.comparator import Dominance
from jmetalpy.core.population import Population

S = TypeVar('S')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BinaryTournament(Selection):

    def __init__(self, comparator: Comparator = Dominance()):
        super(BinaryTournament, self).__init__()
        self.buffer = Queue()
        self.comparator = comparator

    def update(self, *args, **kwargs):
        logger.info("SELECTION update invoked")
        population = kwargs['POPULATION']

        try:
            self.buffer.put(population)
        except Exception as ex:
            print("SELECTION buffer ex: " + str(ex))

    def execute(self, solution_list: Population):
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        if len(solution_list) == 1:
            result = solution_list[0]
        else:
            i, j = random.sample(range(0, len(solution_list)), 2)  # sampling without replacement
            solution1 = solution_list[i]
            solution2 = solution_list[j]

            flag = self.comparator.compare(solution1, solution2)

            if flag == -1:
                result = solution1
            elif flag == 1:
                result = solution2
            else:
                result = [solution1, solution2][random.random() < 0.5]

        return result

    def apply(self, population: Population):
        if not population.is_terminated:
            logger.info("SELECTION: APPLY invoked")

            new_population = Population()
            while len(new_population) < len(population):
                new_population.append(self.execute(population))

            population.mating_pool = new_population

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

    def run(self):
        logger.info("SELECTION: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("SELECTION: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            print("SELECTION ex: " + str(ex))

        logger.info("SELECTION: END RUN")

import logging
from queue import Queue

from jmetalpy.core.operator import Replacement
from jmetalpy.core.population import Population
from jmetalpy.operator.selection import RankingAndCrowdingDistance

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RankingAndCrowding(Replacement):

    def __init__(self):
        super(RankingAndCrowding, self).__init__()
        self.buffer = Queue()

    def update(self, *args, **kwargs):
        logger.info("REPLACEMENT update invoked")
        population = kwargs['POPULATION']

        try:
            self.buffer.put(population)
        except Exception as ex:
            print("REPLACEMENT buffer ex: " + str(ex))

    def apply(self, population: Population):
        if not population.is_terminated:
            logger.info("REPLACEMENT: APPLY invoked")
            join_population = population + population.mating_pool

            selection = RankingAndCrowdingDistance(len(population))

            new_population = Population()
            new_population.extend(selection.execute(join_population))

            new_population.__dict__ = population.__dict__
            new_population.mating_pool = None

            observable_data = {'POPULATION': new_population}
            self.notify_all(**observable_data)
        else:
            observable_data = {'POPULATION': population}
            self.notify_all(**observable_data)

    def run(self):
        logger.info("REPLACEMENT: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("REPLACEMENT: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            print("REPLACEMENT ex: " + str(ex))

        logger.info("REPLACEMENT: END RUN")
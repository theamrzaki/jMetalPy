import logging
from queue import Queue

from jmetalpy.core.algorithm.observable import DefaultObservable
from jmetalpy.core.population import Population
from jmetalpy.core.problem import Problem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RandomInitialSwarm(DefaultObservable):

    def __init__(self, swarm_size: int):
        super(RandomInitialSwarm, self).__init__()
        self.buffer = Queue()
        self.swarm_size = swarm_size

    def apply(self, problem: Problem):
        logger.info("RANDOM_POPULATION_CREATION: Apply invoked")
        swarm = Population()

        for _ in range(0, self.swarm_size):
            swarm.append(problem.create_solution())

        swarm.evaluations = 0
        swarm.leaders = None
        swarm.is_terminated = False
        swarm.problem = problem

        observable_data = {'POPULATION': swarm}
        self.notify_all(**observable_data)

        self.buffer.put(True)

    def run(self):
        logger.info("RANDOM POPULATION CREATOR OBSERVER: RUN")

        try:
            self.buffer.get()
        except Exception as ex:
            print("RANDOM POPULATION ex: " + str(ex))

        logger.info("RANDOM POPULATION CREATOR OBSERVER: END RUN")

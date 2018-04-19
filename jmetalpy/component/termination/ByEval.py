import logging
from queue import Queue

from jmetalpy.core.terminator import Terminator
from jmetalpy.core.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ByEval(Terminator):

    def __init__(self, max_evaluations: int = 1500):
        super(ByEval, self).__init__()
        self.buffer = Queue()
        self.max_evaluations = max_evaluations

    def update(self, *args, **kwargs):
        logger.info("TerminationByEvaluations update invoked")
        population = kwargs["POPULATION"]

        try:
            self.buffer.put(population)
        except Exception as ex:
            print("TERMINATION buffer ex: " + str(ex))

    def apply(self, population: Population):
        evaluations = population.evaluations

        logger.info("TERMINATION. EVALS: " + str(evaluations) + ". MAX: " + str(self.max_evaluations))

        if evaluations >= self.max_evaluations:
            population.is_terminated = True
            logger.info("TERMINATION. ALGORITHM TERMINATED")
        else:
            population.is_terminated = False
            logger.info("EVALUATIONS: " + str(evaluations))

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

    def run(self):
        logger.info("TERMINATION: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("TERMINATION OBSERVER: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            print("TERMINATION ex: " + str(ex))

        logger.info("TERMINATION: END RUN")

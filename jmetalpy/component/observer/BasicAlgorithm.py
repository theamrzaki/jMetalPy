import logging

from jmetalpy.core.algorithm.observable import Observer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasicAlgorithm(Observer):

    def __init__(self, frequency: float = 1.0):
        super(BasicAlgorithm, self).__init__()
        self.display_frequency = frequency

    def update(self, *args, **kwargs):
        population = kwargs["POPULATION"]

        if (population.evaluations % self.display_frequency) == 0:
            print("Evaluations: " + str(population.evaluations) +
                  ". Best fitness: " + str(population[0].objectives))
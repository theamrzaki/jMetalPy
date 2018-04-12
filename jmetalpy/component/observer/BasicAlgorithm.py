import logging

from jmetalpy.core.observable import Observer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasicAlgorithm(Observer):
    def __init__(self, frequency: float = 1.0) -> None:
        self.display_frequency = frequency

    def update(self, *args, **kwargs):
        evaluations = kwargs["evaluations"]

        if (evaluations % self.display_frequency) == 0:
            logger.info("Evaluations: " + str(evaluations) +
                        ". Best fitness: " + str(kwargs["population"][0].objectives) +
                        ". Computing time: " + str(kwargs["computing time"]))

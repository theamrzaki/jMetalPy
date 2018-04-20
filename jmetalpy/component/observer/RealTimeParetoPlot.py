import logging

from jmetalpy.core.algorithm.observable import Observer
from jmetalpy.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RealTimeParetoPlot(Observer):

    def __init__(self, animation_speed: float = 0.0001, frequency: float = 1.0):
        super(RealTimeParetoPlot, self).__init__()
        self.animation_speed = animation_speed
        self.display_frequency = frequency

    def update(self, *args, **kwargs):
        population = kwargs["POPULATION"]
        evaluations = population.evaluations
        computing_time = 1

        if (evaluations % self.display_frequency) == 0:
            SolutionListOutput.plot_scatter_real_time(population, evaluations, computing_time,
                                                      self.animation_speed)

import logging

from jmetalpy.core.observable import Observer
from jmetalpy.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ParetoPlot(Observer):
    def __init__(self, animation_speed: float, frequency: float = 1.0) -> None:
        self.animation_speed = animation_speed
        self.display_frequency = frequency

    def update(self, *args, **kwargs):
        evaluations = kwargs["evaluations"]
        population = kwargs["population"]
        computing_time = kwargs["computing time"]

        if (evaluations % self.display_frequency) == 0:
            SolutionListOutput.plot_scatter_real_time(population, evaluations, computing_time,
                                                      self.animation_speed)

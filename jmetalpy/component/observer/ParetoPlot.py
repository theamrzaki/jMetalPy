import logging

from jmetalpy.core.algorithm.observable import Observer
from jmetalpy.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ParetoPlot(Observer):

    def __init__(self):
        super(ParetoPlot, self).__init__()

    def update(self, *args, **kwargs):
        population = kwargs["POPULATION"]

        if population.is_terminated:
            SolutionListOutput.plot_scatter_to_file(population)

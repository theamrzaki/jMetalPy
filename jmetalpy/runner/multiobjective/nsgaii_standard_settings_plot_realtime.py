import logging
from typing import List

from jmetalpy.algorithm.multiobjective.nsgaii import NSGAII
from jmetalpy.core.solution import FloatSolution
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.operator.selection import BinaryTournament2
from jmetalpy.problem.multiobjective.zdt import ZDT4
from jmetalpy.component.comparator import SolutionAttribute
from jmetalpy.component.observer import ParetoPlot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    problem = ZDT4()
    algorithm = NSGAII[FloatSolution, List[FloatSolution]](
        problem,
        population_size=100,
        max_evaluations=25000,
        mutation=Polynomial(1.0/problem.number_of_variables, distribution_index=20),
        crossover=SBX(1.0, distribution_index=20),
        selection=BinaryTournament2([SolutionAttribute("dominance_ranking"),
                                     SolutionAttribute("crowding_distance", lowest_is_best=False)]))

    observer = ParetoPlot(animation_speed=1 * 10e-8)
    algorithm.observable.register(observer=observer)

    algorithm.run()

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

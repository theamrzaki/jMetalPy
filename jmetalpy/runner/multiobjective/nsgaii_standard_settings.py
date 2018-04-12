import logging
from typing import List

from jmetalpy.algorithm.multiobjective.nsgaii import NSGAII
from jmetalpy.core.solution import FloatSolution
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.operator.selection import BinaryTournament
from jmetalpy.problem.multiobjective.zdt import ZDT1
from jmetalpy.component.evaluator import Sequential, ProcessPool
from jmetalpy.component.comparator import RankingAndCrowdingDistance

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    problem = ZDT1()

    algorithm = NSGAII[FloatSolution, List[FloatSolution]](
        problem=problem,
        population_size=100,
        max_evaluations=25000,
        mutation=Polynomial(1.0/problem.number_of_variables, distribution_index=20),
        crossover=SBX(1.0, distribution_index=20),
        selection=BinaryTournament(RankingAndCrowdingDistance()),
        evaluator=Sequential()
    )

    algorithm.run()

    # SolutionListOutput[FloatSolution].print_function_values_to_file("FUN."+problem.get_name(), algorithm.population)

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())
    logger.info("Computing time: " + str(algorithm.total_computing_time))


if __name__ == '__main__':
    main()

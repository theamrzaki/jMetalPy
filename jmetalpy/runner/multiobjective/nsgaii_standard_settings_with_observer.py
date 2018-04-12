import logging
from typing import List

from jmetalpy.algorithm.multiobjective.nsgaii import NSGAII
from jmetalpy.core.solution import FloatSolution
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.operator.selection import BinaryTournament
from jmetalpy.problem.multiobjective.unconstrained import Kursawe
from jmetalpy.component.comparator import RankingAndCrowdingDistance
from jmetalpy.component.observer import WriteFrontToFile
from jmetalpy.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    problem = Kursawe()
    algorithm = NSGAII[FloatSolution, List[FloatSolution]](
        problem,
        population_size=100,
        max_evaluations=25000,
        mutation=Polynomial(1.0/problem.number_of_variables, distribution_index=20),
        crossover=SBX(1.0, distribution_index=20),
        selection=BinaryTournament(RankingAndCrowdingDistance()))

    observer = WriteFrontToFile("output_directory")
    algorithm.observable.register(observer=observer)

    algorithm.run()
    result = algorithm.get_result()

    SolutionListOutput[FloatSolution].print_function_values_to_file("FUN."+problem.get_name(), result)

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

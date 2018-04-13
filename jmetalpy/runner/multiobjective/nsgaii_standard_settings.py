import logging

from jmetalpy.algorithm.multiobjective.nsgaii import NSGAII
from jmetalpy.component.population import RandomInitialCreation
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.operator.selection import BinaryTournament
from jmetalpy.problem.multiobjective.zdt import ZDT1
from jmetalpy.component.evaluator import Sequential
from jmetalpy.component.comparator import RankingAndCrowdingDistance
from jmetalpy.component.termination import ByEvaluations

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # component creation
    problem = ZDT1()
    initial_population = RandomInitialCreation(population_size=100)
    mutation = Polynomial(1.0/problem.number_of_variables, distribution_index=20)
    crossover = SBX(1.0, distribution_index=20)
    selection = BinaryTournament(RankingAndCrowdingDistance())
    evaluator = Sequential()
    terminator = ByEvaluations(25000)

    # set-up algorithm
    algorithm = NSGAII(
        problem=problem,
        initial_population=initial_population,
        mutation=mutation,
        crossover=crossover,
        selection=selection,
        evaluator=evaluator,
        terminator=terminator
    )

    # run
    algorithm.run()

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

import logging

from jmetalpy.component.archive import Bounded
from jmetalpy.component.observer import BasicAlgorithm, ParetoPlot, RealTimeParetoPlot
from jmetalpy.component.population import RandomInitialPopulation
from jmetalpy.component.variation.CrossoverAndMutation import CrossoverAndMutation
from jmetalpy.component.evaluator import Sequential
from jmetalpy.component.comparator import RankingAndCrowdingDistance
from jmetalpy.component.termination import ByEval
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.algorithm.multiobjective import SMPSO
from jmetalpy.problem.multiobjective.zdt import ZDT1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # component creation
    problem = ZDT1()
    initial_swarm = RandomInitialPopulation(population_size=100)
    mutation = Polynomial(1.0/problem.number_of_variables, distribution_index=20.0)
    evaluator = Sequential()
    terminator = ByEval(max_evaluations=20000)

    # register observers
    terminator.register(RealTimeParetoPlot())
    terminator.register(ParetoPlot())  # will only trigger when the algorithm has finished

    # set up algorithm
    algorithm = SMPSO(
        problem=problem,
        initial_swarm=initial_swarm,
        mutation=mutation,
        evaluator=evaluator,
        terminator=terminator
    )

    # run
    algorithm.run()

    logger.info("Algorithm: " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

import logging

from jmetalpy.component.observer import BasicAlgorithm, ParetoPlot
from jmetalpy.component.population import RandomInitialCreation
from jmetalpy.component.variation.CrossoverAndMutation import CrossoverAndMutation
from jmetalpy.component.evaluator import Sequential
from jmetalpy.component.comparator import RankingAndCrowdingDistance
from jmetalpy.component.termination import ByEval
from jmetalpy.operator.crossover import SBX
from jmetalpy.operator.mutation import Polynomial
from jmetalpy.operator.replacement.RankingAndCrowding import RankingAndCrowding
from jmetalpy.operator.selection import BinaryTournament
from jmetalpy.algorithm.multiobjective.nsgaii import NSGAII
from jmetalpy.problem.multiobjective.zdt import ZDT1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # component creation
    problem = ZDT1()
    initial_population = RandomInitialCreation(population_size=100)
    mutation = Polynomial(1.0/problem.number_of_variables, distribution_index=20.0)
    crossover = SBX(0.9, distribution_index=30.0)
    variation = CrossoverAndMutation(crossover=crossover, mutation=mutation, offspring_population_size=100)
    selection = BinaryTournament(RankingAndCrowdingDistance())
    evaluator = Sequential()
    offspring_evaluator = Sequential()
    terminator = ByEval(max_evaluations=20000)
    replacement = RankingAndCrowding()

    # register observers
    variation.register(BasicAlgorithm())
    terminator.register(ParetoPlot())  # will only trigger when the algorithm has finished

    # set up algorithm
    algorithm = NSGAII(
        problem=problem,
        initial_population=initial_population,
        variation=variation,
        selection=selection,
        replacement=replacement,
        evaluator=evaluator,
        offspring_evaluator=offspring_evaluator,
        terminator=terminator
    )

    # run
    algorithm.run()

    logger.info("Algorithm: " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

import logging

from jmetalpy.algorithm.multiobjective import RandomSearch
from jmetalpy.component.observer import BasicAlgorithm, ParetoPlot, RealTimeParetoPlot
from jmetalpy.component.population import RandomInitialPopulation
from jmetalpy.component.archive import NonDominatedSolutionList
from jmetalpy.component.evaluator import Sequential
from jmetalpy.component.termination import ByEval
from jmetalpy.problem.multiobjective.zdt import ZDT1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # component creation
    problem = ZDT1()
    initial_population = RandomInitialPopulation(population_size=100)
    archive = NonDominatedSolutionList()
    evaluator = Sequential()
    terminator = ByEval(max_evaluations=100)

    # register observers
    terminator.register(ParetoPlot())  # will only trigger when the algorithm has finished

    # set up algorithm
    algorithm = RandomSearch(
        problem=problem,
        initial_population=initial_population,
        archive=archive,
        evaluator=evaluator,
        terminator=terminator
    )

    # run
    algorithm.run()

    logger.info("Algorithm: " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())


if __name__ == '__main__':
    main()

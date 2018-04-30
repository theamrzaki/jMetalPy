import logging
from typing import TypeVar

from jmetalpy.component.population import RandomInitialPopulation
from jmetalpy.core.algorithm import Algorithm
from jmetalpy.core.archive import Archive
from jmetalpy.core.evaluator import Evaluator
from jmetalpy.core.problem import Problem
from jmetalpy.core.terminator import Terminator
from jmetalpy.core.population import Population

S = TypeVar('S')
R = TypeVar(Population)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RandomSearch(Algorithm):

    def __init__(self,
                 problem: Problem,
                 initial_population: RandomInitialPopulation,
                 archive: Archive,
                 evaluator: Evaluator,
                 terminator: Terminator):
        super().__init__()
        self.problem = problem
        self.initial_population = initial_population
        self.archive = archive
        self.evaluator = evaluator
        self.terminator = terminator

    def run(self):
        logger.info("CREATING MAIN LOOP...")
        self.initial_population.register(self.terminator)
        self.terminator.register(self.evaluator)
        self.evaluator.register(self.archive)
        self.archive.register(self.terminator)

        logger.info("STARTING THREADS...")
        self.initial_population.start()
        self.evaluator.start()
        self.archive.start()
        self.terminator.start()

        # start the algorithm
        logger.info("...OK! RUNNING RANDOM SEARCH")
        self.initial_population.apply(self.problem)

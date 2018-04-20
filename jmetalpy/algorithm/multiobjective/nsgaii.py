import logging
from typing import TypeVar

from jmetalpy.component.population import RandomInitialPopulation
from jmetalpy.core.algorithm import Algorithm
from jmetalpy.core.evaluator import Evaluator
from jmetalpy.core.operator import Selection, Replacement, Operator
from jmetalpy.core.problem import Problem
from jmetalpy.core.terminator import Terminator
from jmetalpy.core.population import Population

S = TypeVar('S')
R = TypeVar(Population)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NSGAII(Algorithm):

    def __init__(self,
                 problem: Problem,
                 initial_population: RandomInitialPopulation,
                 variation: Operator,
                 selection: Selection,
                 replacement: Replacement,
                 evaluator: Evaluator,
                 offspring_evaluator: Evaluator,
                 terminator: Terminator):
        super().__init__()
        self.problem = problem
        self.initial_population = initial_population
        self.variation = variation
        self.selection = selection
        self.replacement = replacement
        self.evaluator = evaluator
        self.offspring_evaluator = offspring_evaluator
        self.terminator = terminator

    def run(self):
        logger.info("ADDING COMPONENTS...")
        self.initial_population.register(self.evaluator)
        self.evaluator.register(self.terminator)

        logger.info("CREATING MAIN LOOP...")
        self.terminator.register(self.selection)
        self.selection.register(self.variation)
        self.variation.register(self.offspring_evaluator)
        self.offspring_evaluator.register(self.replacement)
        self.replacement.register(self.terminator)

        logger.info("STARTING THREADS...")
        self.initial_population.start()
        self.evaluator.start()
        self.terminator.start()
        self.selection.start()
        self.variation.start()
        self.offspring_evaluator.start()
        self.replacement.start()

        # start the algorithm
        logger.info("...OK! RUNNING NSGA-II")
        self.initial_population.apply(self.problem)


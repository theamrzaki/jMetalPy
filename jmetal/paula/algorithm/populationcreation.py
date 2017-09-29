import logging
import threading
import time
from typing import TypeVar, Generic, List

from jmetal.core.algorithm import Algorithm
from jmetal.core.problem import Problem
from jmetal.core.solution import FloatSolution
from jmetal.component.evaluator import Evaluator, SequentialEvaluator
from jmetal.paula.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')


class PopulationCreation(Generic[S]):
    """
    Class representing entities that create populations of a given size
    """
    def __init__(self, problem: Problem[S], population_size: int):
        self.problem = problem
        self.population_size = population_size

    def apply(self) -> Population[S]:
        pass


class SequentialRandomPopulationCreation(PopulationCreation[S]):
    def __init__(self, problem: Problem[S], population_size: int):
        super(SequentialEvaluator, self).__init(problem, population_size)

    def apply(self) -> Population[S]:
        population : Population[S] = Population[S]
        for i in range(self.population_size):
            population.append(self.problem.create_solution())


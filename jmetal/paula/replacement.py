import logging
import threading
import time
from typing import TypeVar, Generic, List

from jmetal.core.algorithm import Algorithm
from jmetal.core.problem import Problem
from jmetal.core.solution import FloatSolution
from jmetal.component.evaluator import Evaluator, SequentialEvaluator
from jmetal.paula.population import Population
from jmetal.paula.populationcreation import PopulationCreation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')


class Replacement(Generic[S]):
    def __init__(self):
        pass

    def apply(self, population: Population[S], offspring_population: Population[S]) -> Population[S]:
        pass

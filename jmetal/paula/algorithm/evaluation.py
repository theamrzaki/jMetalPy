import logging
from typing import TypeVar, Generic

from jmetal.core.problem import Problem
from jmetal.paula.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')


class Evaluation(Generic[S]):
    def __init__(self):
        pass

    def apply(self, problem: Problem[S], population: Population[S]) -> Population[S]:
        pass

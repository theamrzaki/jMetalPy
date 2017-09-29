import logging
from typing import TypeVar, Generic

from jmetal.paula.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')


class MatingPool(Generic[S]):
    def __init__(self):
        pass

    def apply(self, population: Population[S]) -> Population[S]:
        pass

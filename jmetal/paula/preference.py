import logging
from typing import TypeVar, Generic, List

from jmetal.core.problem import Problem
from jmetal.paula.population import Population
from jmetal.util.comparator import Comparator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')


class Partitioning(Generic[S]):
    def apply(self, population: Population[S]) -> List[Population[S]]:
        pass


class Preference(Generic[S]):
    """ A preference is a relation among the solutions of a population in such a way that the solutions are assigned
    an attribute that represents their corresponding associated value according to the preference.

    After applying a preference, the solutions can be compared based on their preference attribute values.

    """

    def apply(self, population: Population[S]) -> Population[S]:
        pass

    def get_comparator(self) -> Comparator:
        pass


class SetPartitioning(Preference[S]):
    pass


class diversity(Preference[S]):
    pass
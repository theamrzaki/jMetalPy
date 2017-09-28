import logging
from typing import TypeVar, Generic, List

from jmetal.core.problem import Problem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')

class Population(List[S]):
    def __init__(self, list: List[S] = []):
        for value in list:
            self.append(value)
        pass


list = [4, 5, 6, 7, 7]
list.append(5)
print(list)
pop = Population(list)
pop.append(4)
pop.append(5)
setattr(pop, "c", 324)
print(len(pop))
print(pop)
print(getattr(pop, "c"))
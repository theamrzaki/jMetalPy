from typing import TypeVar

from jmetalpy.core.solution import Solution
from jmetalpy.core.comparator import Comparator

S = TypeVar('S')


class SolutionAttribute(Comparator):

    def __init__(self, key: str, lowest_is_best: bool = True):
        super().__init__()
        self.key = key
        self.lowest_is_best = lowest_is_best

    def compare(self, solution_1: Solution, solution_2: Solution) -> int:
        value_1 = solution_1.attributes.get(self.key)
        value_2 = solution_2.attributes.get(self.key)

        result = 0
        if value_1 is not None and value_2 is not None:
            if self.lowest_is_best:
                if value_1 < value_2:
                    result = -1
                elif value_1 > value_2:
                    result = 1
                else:
                    result = 0
            else:
                if value_1 > value_2:
                    result = -1
                elif value_1 < value_2:
                    result = 1
                else:
                    result = 0

        return result

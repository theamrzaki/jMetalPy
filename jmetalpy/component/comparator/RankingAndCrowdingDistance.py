from typing import TypeVar

from jmetalpy.core.solution import Solution
from jmetalpy.core.comparator import Comparator
from jmetalpy.component.comparator import SolutionAttribute

S = TypeVar('S')


class RankingAndCrowdingDistance(Comparator):

    def compare(self, solution1: Solution, solution2: Solution) -> int:
        result = \
            SolutionAttribute("dominance_ranking").compare(solution1, solution2)

        if result is 0:
            result = \
                SolutionAttribute("crowding_distance", lowest_is_best=False).compare(solution1, solution2)

        return result

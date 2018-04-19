from typing import List, TypeVar

from jmetalpy.core.operator import Selection
from jmetalpy.component.comparator import Dominance
from jmetalpy.core.population import Population

S = TypeVar('S')


class BestSolution(Selection):

    def execute(self, solution_list: Population) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        result = solution_list[0]
        for solution in solution_list[1:]:
            if Dominance().compare(solution, result) < 0:
                result = solution

        return result

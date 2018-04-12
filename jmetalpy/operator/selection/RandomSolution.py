import random
from typing import List, TypeVar

from jmetalpy.core.operator import Selection

S = TypeVar('S')


class RandomSolutionSelection(Selection[List[S], S]):
    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        return random.choice(solution_list)


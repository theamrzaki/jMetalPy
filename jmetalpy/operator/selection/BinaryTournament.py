import random
from typing import List, TypeVar

from jmetalpy.core.operator import Selection
from jmetalpy.core.comparator import Comparator
from jmetalpy.component.comparator import Dominance


S = TypeVar('S')


class BinaryTournament(Selection):
    def __init__(self, comparator: Comparator = Dominance()):
        super().__init__()
        self.comparator = comparator

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        if len(solution_list) == 1:
            result = solution_list[0]
        else:
            i, j = random.sample(range(0, len(solution_list)), 2)  # sampling without replacement
            solution1 = solution_list[i]
            solution2 = solution_list[j]

            flag = self.comparator.compare(solution1, solution2)

            if flag == -1:
                result = solution1
            elif flag == 1:
                result = solution2
            else:
                result = [solution1, solution2][random.random() < 0.5]

        return result

    def get_name(self) -> str:
        return "Binary tournament selection"
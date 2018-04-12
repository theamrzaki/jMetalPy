import random
from typing import List, TypeVar

from jmetalpy.core.operator import Selection
from jmetalpy.core.comparator import Comparator

S = TypeVar('S')


class BinaryTournament2(Selection[List[S], S]):
    def __init__(self, comparator_list: List[Comparator]):
        self.comparator_list = comparator_list

    def get_name(self):
        return "Binary tournament selection (experimental)"

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")
        elif not self.comparator_list:
            raise Exception("The list of comparators is empty")

        winner = None

        if len(solution_list) == 1:
            winner = solution_list[0]
        else:
            for comparator in self.comparator_list:
                winner = self.__winner(solution_list, comparator)
                if winner is not None:
                    break

        if not winner:
            i = random.randrange(0, len(solution_list))
            winner = solution_list[i]

        return winner

    def __winner(self, solution_list: List[S], comparator: Comparator):
        i, j = random.sample(range(0, len(solution_list)), 2)  # sampling without replacement
        solution1 = solution_list[i]
        solution2 = solution_list[j]

        flag = comparator.compare(solution1, solution2)

        if flag == -1:
            result = solution1
        elif flag == 1:
            result = solution2
        else:
            result = None

        return result

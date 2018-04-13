import random
from typing import List, TypeVar

from jmetalpy.core.operator import Selection

S = TypeVar('S')


class NaryRandomSolutionSelection(Selection):
    def __init__(self, number_of_solutions_to_be_returned: int = 1):
        super().__init__()
        if number_of_solutions_to_be_returned < 0:
            raise Exception("The number of solutions to be returned must be positive integer")

        self.number_of_solutions_to_be_returned = number_of_solutions_to_be_returned

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        if len(solution_list) == 0:
            raise Exception("The solution is empty")
        if len(solution_list)<self.number_of_solutions_to_be_returned:
            raise Exception("The solution list contains less elements then requred")

        # random sampling without replacement
        return random.sample(solution_list, self.number_of_solutions_to_be_returned)

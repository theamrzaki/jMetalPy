import copy
from typing import List

from jmetalpy.core.operator import Crossover
from jmetalpy.core.solution import Solution


class Null(Crossover):
    def __init__(self):
        super(Null, self).__init__(probability=0)

    def execute(self, parents: List[Solution]) -> List[Solution]:
        if len(parents) != 2:
            raise Exception("The number of parents is not two: " + str(len(parents)))

        return [copy.deepcopy(parents[0]), copy.deepcopy(parents[1])]

    def get_number_of_parents(self):
        return 2
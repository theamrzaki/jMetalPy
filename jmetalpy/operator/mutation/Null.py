from jmetalpy.core.operator import Mutation
from jmetalpy.core.solution import Solution


class Null(Mutation):

    def __init__(self):
        super(Null, self).__init__(probability=0)

    def get_name(self):
        return "Null mutation"

    def execute(self, solution: Solution) -> Solution:
        return solution

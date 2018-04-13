from typing import TypeVar, List
from multiprocessing.pool import ThreadPool

from jmetalpy.core.problem import Problem
from jmetalpy.core.evaluator import Evaluator

S = TypeVar('S')


class Parallel(Evaluator):
    def __init__(self, processes: int = 4):
        super().__init__()
        self.pool = ThreadPool(processes)

    def evaluate(self, solution_list: List[S], problem: Problem) -> List[S]:
        self.pool.map(lambda solution: Evaluator.evaluate_solution(solution, problem), solution_list)
        return solution_list

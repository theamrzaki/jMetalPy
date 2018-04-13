from typing import TypeVar, List
from multiprocessing.pool import ThreadPool
from dask.distributed import Client

from jmetal.core.problem import Problem
from jmetalpy.core.evaluator import Evaluator


S = TypeVar('S')


class DaskParallel(Evaluator):

    def __init__(self, processes: int = 4):
        super().__init__()
        self.pool = ThreadPool(processes)
        self.client = Client()

    def evaluate(self, solution_list: List[S], problem: Problem) -> List[S]:
        futures = [self.client.submit(Evaluator.evaluate_solution, solution, problem) for solution in solution_list]
        self.client.gather(futures)
        return solution_list

from typing import TypeVar, List
from concurrent.futures import ProcessPoolExecutor

from jmetalpy.core.problem import Problem
from jmetalpy.core.evaluator import Evaluator

S = TypeVar('S')


class Submit:

    def __init__(self, submit_func):
        self.submit_func = submit_func

    def evaluate(self, solution_list: List[S], problem: Problem) -> List[S]:
        futures = [self.submit_func(Evaluator.evaluate_solution, solution, problem) for solution in solution_list]
        return [f.result() for f in futures]


class ProcessPool(Submit):

    def __init__(self, processes: int=4):
        self.executor = ProcessPoolExecutor(processes)
        super(ProcessPool, self).__init__(self.executor.submit)

    def close(self):
        self.executor.shutdown()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

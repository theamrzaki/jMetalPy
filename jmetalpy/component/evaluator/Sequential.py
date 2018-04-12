from typing import TypeVar, List

from jmetalpy.core.problem import Problem
from jmetalpy.core.evaluator import Evaluator

S = TypeVar('S')


class Sequential(Evaluator[S]):
    def evaluate(self, solution_list: List[S], problem: Problem) -> List[S]:
        unevaluated_list = [solution for solution in solution_list if not solution.evaluated]

        for unevaluated in unevaluated_list:
            Evaluator.evaluate_solution(unevaluated, problem)
            unevaluated.evaluated = True

        return solution_list
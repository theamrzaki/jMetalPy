import unittest

from jmetalpy.component.evaluator import DaskParallel
from jmetalpy.problem.multiobjective.zdt import ZDT1


class ParrallelEvaluatorTestCases(unittest.TestCase):
    def test_should_evaluate_solutions_in_parallel(self):
        """
        problem = ZDT1(4)
        solution_list = [problem.create_solution(), problem.create_solution(),
                         problem.create_solution(), problem.create_solution()]

        dask_evaluator = DaskParallel()
        dask_evaluator.evaluate(solution_list, problem)
        
        print(solution_list[0].objectives)
        """
        pass


if __name__ == '__main__':
    unittest.main()

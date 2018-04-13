from typing import TypeVar

from jmetalpy.core.archive import Archive
from jmetalpy.component.comparator import Dominance, EqualSolutions

S = TypeVar('S')


class NonDominatedSolutionList(Archive):
    def __init__(self):
        super(NonDominatedSolutionList, self).__init__()
        self.comparator = Dominance()

    def add(self, solution:S) -> bool:
        is_dominated = False
        is_contained = False

        if len(self.solution_list) == 0:
            self.solution_list.append(solution)
            return True
        else:
            number_of_deleted_solutions = 0

            # New copy of list and enumerate
            for index, current_solution in enumerate(list(self.solution_list)):
                is_dominated_flag = self.comparator.compare(solution, current_solution)
                if is_dominated_flag == -1:
                    del self.solution_list[index-number_of_deleted_solutions]
                    number_of_deleted_solutions += 1
                elif is_dominated_flag == 1:
                    is_dominated = True
                    break
                elif is_dominated_flag == 0:
                    if EqualSolutions().compare(solution, current_solution) == 0:
                        is_contained = True
                        break

        if not is_dominated and not is_contained:
            self.solution_list.append(solution)
            return True

        return False

    def get_comparator(self):
        return self.comparator

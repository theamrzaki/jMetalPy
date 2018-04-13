from typing import TypeVar, List

S = TypeVar('S')


class Archive:

    def __init__(self):
        super().__init__()
        self.solution_list: List[S] = []

    def add(self, solution: S) -> bool:
        pass

    def get(self, index: int) -> S:
        return self.solution_list[index]

    def get_solution_list(self) -> List[S]:
        return self.solution_list

    def size(self) -> int:
        return len(self.solution_list)

    def get_comparator(self):
        pass

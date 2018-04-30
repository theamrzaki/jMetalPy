from typing import TypeVar, List

from jmetalpy.core.algorithm.observable import DefaultObservable, Observer, Observable

S = TypeVar('S')


class Archive(DefaultObservable, Observer):

    def __init__(self):
        super(Archive, self).__init__()
        self.observable: Observable = DefaultObservable()
        self.solution_list: List[S] = []

    def update(self, *args, **kwargs):
        pass

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

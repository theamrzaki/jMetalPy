from typing import TypeVar

from jmetalpy.core.archive import Archive

S = TypeVar('S')


class Bounded(Archive[S]):
    def __init__(self, maximum_size: int):
        super(Bounded, self).__init__()
        self.maximum_size = maximum_size

    def get_max_size(self) -> int:
        return self.maximum_size

    def compute_density_estimator(self):
        pass

    def sort(self):
        pass
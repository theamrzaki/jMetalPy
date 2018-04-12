from typing import TypeVar

S = TypeVar('S')


class Comparator:
    def compare(self, object1: S, object2: S) -> int:
        pass

import threading
from typing import TypeVar

S = TypeVar('S')


class Comparator(threading.Thread):

    def compare(self, object1: S, object2: S) -> int:
        pass

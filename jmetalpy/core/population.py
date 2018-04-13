import threading
from typing import TypeVar

S = TypeVar('S')


class Population(threading.Thread):

    def __init__(self):
        super(Population, self).__init__()

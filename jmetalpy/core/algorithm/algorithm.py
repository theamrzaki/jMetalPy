import logging
import threading
import time
from typing import TypeVar

from jmetalpy.core.algorithm.observable import DefaultObservable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')
R = TypeVar('R')


class Algorithm(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.observable = DefaultObservable()
        self.start_computing_time: int = 0
        self.total_computing_time: int = 0

    def get_name(self) -> str:
        return type(self).__name__

    def get_current_computing_time(self) -> float:
        return time.time() - self.start_computing_time

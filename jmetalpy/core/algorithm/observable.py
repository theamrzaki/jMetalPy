import threading
from abc import ABCMeta, abstractmethod


class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Observable(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def register(self, observer):
        pass

    def deregister(self, observer):
        pass

    def deregister_all(self):
        pass

    def notify_all(self, *args, **kwargs):
        pass


class DefaultObservable(Observable):

    def __init__(self):
        super(DefaultObservable, self).__init__()
        self.observers = []

    def register(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def deregister(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def deregister_all(self):
        if self.observers:
            del self.observers[:]

    def notify_all(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

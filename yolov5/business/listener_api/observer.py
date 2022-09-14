from abc import ABC, abstractmethod
from observables.observable import Observable


class Observer(ABC):

    @abstractmethod
    def update(self, observable: Observable):
        pass
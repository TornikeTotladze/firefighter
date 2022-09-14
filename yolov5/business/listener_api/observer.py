from abc import ABC, abstractmethod
from business.listener_api.observable import Observable


class Observer(ABC):

    @abstractmethod
    def update(self, observable: Observable):
        pass
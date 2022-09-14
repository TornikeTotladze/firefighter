from abc import ABC, abstractmethod
from yolov5.observers.observer import Observer

class Observable(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass


    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass


    @abstractmethod
    def notify(self) -> None:
        pass
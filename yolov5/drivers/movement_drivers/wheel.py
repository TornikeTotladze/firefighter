from abc import ABC, abstractmethod


class Wheel(ABC):

    @abstractmethod
    def forward(self, step: int) -> None:
        pass

    @abstractmethod
    def backward(self, step: int) -> None:
        pass

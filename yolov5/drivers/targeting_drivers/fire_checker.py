from abc import ABC, abstractmethod


class FireChecker(ABC):

    @abstractmethod
    def fire_presented(self) -> bool:
        pass

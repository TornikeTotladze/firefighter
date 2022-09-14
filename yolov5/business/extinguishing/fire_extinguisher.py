from abc import ABC, abstractmethod


class FireExtinguisher(ABC):

    @abstractmethod
    def extinguish(self, duration_in_ms: int) -> None:
        pass
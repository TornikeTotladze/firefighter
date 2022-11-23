from abc import ABC, abstractmethod


class TargetChecker(ABC):
    
    @abstractmethod
    def target_is_presented(self) -> bool:
        pass

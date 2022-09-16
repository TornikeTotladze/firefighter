from abc import ABC, abstractmethod


class TargetDto(ABC):
    
    @abstractmethod
    def get_name(self) -> str:
        pass
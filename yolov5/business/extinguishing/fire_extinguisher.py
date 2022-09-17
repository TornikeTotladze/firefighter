from abc import ABC, abstractmethod
from business.dto.target_dto import TargetDto


class FireExtinguisher(ABC):

    @abstractmethod
    def extinguish(self, target_dto: TargetDto) -> None:
        pass
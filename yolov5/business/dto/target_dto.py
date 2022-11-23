from abc import ABC, abstractmethod


class TargetDto(ABC):

    @abstractmethod
    def get_center_x(self) -> str:
        return self.__center_x

    @abstractmethod
    def get_center_y(self) -> str:
        return self.__center_y

    @abstractmethod
    def get_area(self) -> str:
        return self.__area

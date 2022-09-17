from business.dto.target_dto import TargetDto


class FireDto(TargetDto):
    

    def __init__(self, center_x: float, center_y: float, area: float) -> None:
        self.__center_x: float = center_x
        self.__center_y: float = center_y
        self.__area: float = area


    def get_center_x(self) -> str:
        return self.__center_x


    def get_center_y(self) -> str:
        return self.__center_y


    def get_area(self) -> str:
        return self.__area
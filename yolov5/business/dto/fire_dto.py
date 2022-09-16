from business.dto.target_dto import TargetDto


class FireDto(TargetDto):
    

    def __init__(self, name: str) -> None:
        self.__name = name


    def get_name(self) -> str:
        return self.__name
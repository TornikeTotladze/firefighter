from business.targeting.barrel import Barrel
from drivers.targeting_drivers.tube import Tube
from drivers.targeting_drivers.water_tube import WaterTube
from business.dto.target_dto import TargetDto


class WaterJetBarrel(Barrel):
    
    def __init__(self) -> None:
        self.__tube: Tube = WaterTube()


    def stand_on_corresponding_angle(self, targetDto: TargetDto) -> None:
        # calculate correct angle
        angle: float = 12

        self.__tube.write_angle(angle)
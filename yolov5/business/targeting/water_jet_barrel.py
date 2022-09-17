from time import sleep
from business.targeting.barrel import Barrel
from drivers.targeting_drivers.tube import Tube
from drivers.targeting_drivers.water_tube import WaterTube
from business.dto.target_dto import TargetDto


class WaterJetBarrel(Barrel):
    
    def __init__(self) -> None:
        self.__tube: Tube = WaterTube()


    def stand_on_corresponding_angle(self, target_dto: TargetDto) -> None:
        # calculate correct angle
        print("Waret jet barrel area: " + str(target_dto.get_area()))
        if (target_dto.get_area() >= 5000):
            self.__stand_on_y(target_dto.get_center_y())

        
        


    def __stand_on_y(self, center_y: float):
        self.__tube.write_angle(-50)
        sleep(0.5)
        self.__tube.write_angle(-20)
from math import atan, pi
from time import sleep
from business.targeting.barrel import Barrel
from business.targeting.ir_target_checker import IRTargetChecker
from business.targeting.target_checker import TargetChecker
from configuration.constants import TARGET_AREA_THRESHOLD
from drivers.targeting_drivers.water_tube import servo_max_angle
from drivers.targeting_drivers.water_tube import servo_min_angle
from drivers.targeting_drivers.tube import Tube
from drivers.targeting_drivers.water_tube import WaterTube
from business.dto.target_dto import TargetDto


class WaterJetBarrel(Barrel):
    
    def __init__(self) -> None:
        self.__tube: Tube = WaterTube()
        self.__target_checker: TargetChecker = IRTargetChecker()


    def stand_on_corresponding_angle(self, target_dto: TargetDto) -> None:

        if (target_dto.get_center_x() >= 310 and target_dto.get_center_x() <= 330 
                and target_dto.get_area() >= TARGET_AREA_THRESHOLD):
            self.__stand_on_y(target_dto.get_center_y())
            print(target_dto.get_center_y())

        
    def __stand_on_y(self, center_y: float):
        # angle: float = -65 + 180 / pi * atan((260 - center_y) * 0.35 / 640 / 0.28)
        angle: float = servo_max_angle 

        while (not self.__target_checker.target_is_presented() and angle > servo_min_angle):
            self.__tube.write_angle(angle)
            sleep(0.2)
            angle -= 5

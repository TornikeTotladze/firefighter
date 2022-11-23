from business.dto.target_dto import TargetDto
from business.extinguishing.fire_extinguisher import FireExtinguisher
from business.targeting.ir_target_checker import IRTargetChecker
from business.targeting.target_checker import TargetChecker
from configuration.constants import TARGET_AREA_THRESHOLD
from drivers.targeting_drivers.pump import Pump
from drivers.targeting_drivers.water_pump import WaterPump


class WaterJetFireExtinguisher(FireExtinguisher):

    def __init__(self) -> None:
        self.__pump: Pump = WaterPump(10, 9, 22)
        self.__target_checker: TargetChecker = IRTargetChecker()
        pass

    def extinguish(self, target_dto: TargetDto) -> None:
        print("Waret jet extinguisher area: " + str(target_dto.get_area()))
        if (target_dto.get_center_x() >= 310 and target_dto.get_center_x() <= 330
                and target_dto.get_area() >= TARGET_AREA_THRESHOLD):

            while self.__target_checker.target_is_presented():
                self.__pump.inject(4000)

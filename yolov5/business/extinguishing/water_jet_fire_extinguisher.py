from business.dto.target_dto import TargetDto
from business.extinguishing.fire_extinguisher import FireExtinguisher
from drivers.targeting_drivers.pump import Pump
from drivers.targeting_drivers.water_pump import WaterPump


class WaterJetFireExtinguisher(FireExtinguisher):

    def __init__(self) -> None:
        self._pump: Pump = WaterPump(10, 9, 22)
        pass


    def extinguish(self, target_dto: TargetDto) -> None:
        print("Waret jet extinguisher area: " + str(target_dto.get_area()))
        if (target_dto.get_area() >= 5000):
            self._pump.inject(2000)


from business.extinguishing.fire_extinguisher import FireExtinguisher
from drivers.targeting_drivers.pump import Pump
from drivers.targeting_drivers.water_pump import WaterPump


class WaterJetFireExtinguisher(FireExtinguisher):

    def __init__(self) -> None:
        self.pump: Pump = WaterPump()
        pass


    def extinguish(self, duration_in_ms: int) -> None:
        self.pump.inject(duration_in_ms)
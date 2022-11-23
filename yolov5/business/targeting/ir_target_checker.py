from business.targeting.target_checker import TargetChecker
from drivers.targeting_drivers.fire_checker import FireChecker
from drivers.targeting_drivers.flame_sensor import FlameSensor

fire_sensor_pi = 20


class IRTargetChecker(TargetChecker):

    def __init__(self) -> None:
        self.__fire_checker: FireChecker = FlameSensor(fire_sensor_pi)

    def target_is_presented(self) -> bool:
        return self.__fire_checker.fire_presented()

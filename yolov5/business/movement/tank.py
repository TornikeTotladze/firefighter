from time import sleep, time
from business.dto.target_dto import TargetDto
from business.movement.cart import Cart
from configuration.constants import OBSTACLE_AVOID_BACK, OBSTACLE_AVOID_DISTANCE, ROTATION_ANGLE_AT_OBSTACLE, \
    ROTATION_ANGLE_STEP, TARGET_AREA_THRESHOLD
from drivers.movement_drivers.obstacle_detector import ObstacleDetector
from drivers.movement_drivers.sonic_sensor import SonicSensor
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle

MIN_DISTANCE_TO_OBSTACLE = 15.0
DIFF_BETWEEN_DISTANCES = 5.0


class Tank(Cart):

    def __init__(self) -> None:
        self.__left_obstacle_detector: ObstacleDetector = SonicSensor(trig_pin=25, echo_pin=24)
        self.__right_obstacle_detector: ObstacleDetector = SonicSensor(trig_pin=7, echo_pin=8)
        self.__vehicle: Vehicle = CaterpillarVehicle()

    def move_to_target(self, target_dto: TargetDto) -> None:
        if target_dto.get_area() < TARGET_AREA_THRESHOLD:
            if target_dto.get_center_x() > 370:
                self.__vehicle.turn_right(ROTATION_ANGLE_STEP)
            elif target_dto.get_center_x() < 270:
                self.__vehicle.turn_left(ROTATION_ANGLE_STEP)
            else:
                self.__move_forward()
        else:
            if target_dto.get_center_x() > 330:
                self.__vehicle.turn_right(5)
            elif target_dto.get_center_x() < 310:
                self.__vehicle.turn_left(5)

    def rotate(self) -> None:
        self.__vehicle.turn_left(ROTATION_ANGLE_STEP)

    def __move_forward(self):
        l = self.__left_obstacle_detector.distance_to_obstacle()
        r = self.__right_obstacle_detector.distance_to_obstacle()

        print("left obstcle at: " + str(l))
        print("right obstcle at: " + str(r))
        if l <= MIN_DISTANCE_TO_OBSTACLE or r <= MIN_DISTANCE_TO_OBSTACLE:
            if r >= l + MIN_DISTANCE_TO_OBSTACLE:
                self.__vehicle.backward(OBSTACLE_AVOID_BACK)
                sleep(0.4)
                self.__vehicle.turn_right(ROTATION_ANGLE_AT_OBSTACLE)
                sleep(0.4)
                self.__vehicle.forward(OBSTACLE_AVOID_DISTANCE)
                sleep(0.4)
                self.__vehicle.turn_left(1.3 * ROTATION_ANGLE_AT_OBSTACLE)
                sleep(0.4)
                self.__vehicle.forward(OBSTACLE_AVOID_DISTANCE)
            # sleep(0.4)
            # self.__vehicle.turn_right(ROTATION_ANGLE_AT_OBSTACLE)
            elif l >= r + MIN_DISTANCE_TO_OBSTACLE:
                self.__vehicle.backward(OBSTACLE_AVOID_BACK)
                sleep(0.4)
                self.__vehicle.turn_left(ROTATION_ANGLE_AT_OBSTACLE)
                sleep(0.4)
                self.__vehicle.forward(OBSTACLE_AVOID_DISTANCE)
                sleep(0.4)
                self.__vehicle.turn_right(1.3 * ROTATION_ANGLE_AT_OBSTACLE)
                sleep(0.4)
                self.__vehicle.forward(OBSTACLE_AVOID_DISTANCE)
            # sleep(0.4)
            # self.__vehicle.turn_left(ROTATION_ANGLE_AT_OBSTACLE)
        else:
            self.__vehicle.forward(300)

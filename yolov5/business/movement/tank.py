from time import sleep, time
from business.dto.target_dto import TargetDto
from business.movement.cart import Cart
from drivers.movement_drivers.obstacle_detector import ObstacleDetector
from drivers.movement_drivers.sonic_sensor import SonicSensor
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle


MIN_DISTANCE_TO_OBSTACLE = 15.0
DIFF_BETWEEN_DISTANCES = 5.0

class Tank(Cart):

	def __init__(self) -> None:
		self.__left_obstacle_detector: ObstacleDetector = SonicSensor(trig_pin = 25, echo_pin = 24)
		self.__right_obstacle_detector: ObstacleDetector = SonicSensor(trig_pin = 7, echo_pin = 8)
		self.__vehicle: Vehicle = CaterpillarVehicle()


	def move_to_target(self, target_dto: TargetDto) -> None:
		print("tank area: " + str(target_dto.get_area()))
		# do something to arive at target
		#self.__stand_on_x(target_dto.get_center_x())

		if (target_dto.get_area() < 5000):
			if target_dto.get_center_x() > 350:
				self.__vehicle.turn_right(7)
			elif target_dto.get_center_x() < 290:
				self.__vehicle.turn_left(7)
			else:
				self.__move_forward()


	def __move_forward(self):
		l = self.__left_obstacle_detector.distanceToObstacle()
		r = self.__right_obstacle_detector.distanceToObstacle()

		print("left obstcle at: " + str(l))
		print("right obstcle at: " + str(r))
		if (l <= MIN_DISTANCE_TO_OBSTACLE or r <= MIN_DISTANCE_TO_OBSTACLE):
			if (r >= l + MIN_DISTANCE_TO_OBSTACLE):
				self.__vehicle.turn_right(50)
				sleep(0.2)
				self.__vehicle.forward(400)
				sleep(0.2)
				self.__vehicle.turn_left(50)
				sleep(0.2)
				self.__vehicle.forward(400)
			elif (l >= r + MIN_DISTANCE_TO_OBSTACLE):
				self.__vehicle.turn_left(50)
				sleep(0.2)
				self.__vehicle.forward(400)
				sleep(0.2)
				self.__vehicle.turn_right(50)
				sleep(0.2)
				self.__vehicle.forward(400)
		# 	else:
		# 		self.__vehicle.backward(200)
		else:
			self.__vehicle.forward(300)
		# self.__vehicle.forward(200)
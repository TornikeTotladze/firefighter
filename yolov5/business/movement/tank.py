from time import sleep
from business.dto.target_dto import TargetDto
from business.movement.cart import Cart
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle


class Tank(Cart):

	def __init__(self) -> None:
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
				self.__vehicle.forward(200)


	def __stand_on_x(self, center_x: float):
		pass

from time import sleep
from business.dto.target_dto import TargetDto
from business.movement.cart import Cart
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle


class Tank(Cart):

	def __init__(self) -> None:
		self.__vehicle: Vehicle = CaterpillarVehicle()


	def move_to_target(self, targetDto: TargetDto) -> None:
		# do something to arive at target
		print("tank is moving to target: " + targetDto.get_name())
		self.__vehicle.forward(500)
		sleep(0.5)
		self.__vehicle.backward(900)
		pass


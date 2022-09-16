from business.dto.target_dto import TargetDto
from business.movement.cart import Cart
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle


class Tank(Cart):

	def __init__(self) -> None:
		self.__vehicle: Vehicle = CaterpillarVehicle()


	def move_to_target(targetDto: TargetDto) -> None:
		# do something to arive at target
		pass


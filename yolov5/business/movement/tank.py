from ast import List
from business.movement.cart import Cart
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle
from business.listener_api.observer import Observer
from business.listener_api.observable import Observable
from business.listener_api.general import General


class Tank():

	def __init__(self) -> None:
		self.vehicle: Vehicle = CaterpillarVehicle()
		super.__init__()


	def go_forward(self, dist: float) -> None:
		self.vehicle.forward(dist)


	def go_backward(self, dist: float) -> None:
		self.vehicle.backward(dist)


	def turn_left(self, angle: float) -> None:
		self.vehicle.turn_left(angle)


	def turn_right(self, angle: float) -> None:
		self.vehicle.turn_right(angle)

	
	def attach(self, observer: Observer) -> None:
		self._observers.append(observer)
			

	def detach(self, observer: Observer) -> None:
		self._observers.remove(observer)


	def notify(self) -> None:
		for observer in self._observers:
			observer.update(self)


	def update(self, observable: Observable):
		# do move algorithm
		pass
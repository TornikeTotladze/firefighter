from abc import ABC, abstractmethod
from business.listener_api.observer import Observer
from business.listener_api.observable import Observable


class Cart(Observer, Observable, ABC):
	
	@abstractmethod
	def go_forward(self, dist: float) -> None:
		pass


	@abstractmethod
	def go_backward(self, dist: float) -> None:
		pass


	@abstractmethod
	def turn_left(self, angle: float) -> None:
		pass


	@abstractmethod
	def turn_right(self, angle: float) -> None:
		pass
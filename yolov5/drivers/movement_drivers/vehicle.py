from abc import ABC, abstractmethod


class Vehicle(ABC):

	@abstractmethod
	def forward(self, dist: float) -> None:
		pass


	@abstractmethod
	def backward(self, dist: float) -> None:
		pass


	@abstractmethod
	def turn_left(self, angle: float) -> None:
		pass


	@abstractmethod
	def turn_right(self, angle: float) -> None:
		pass

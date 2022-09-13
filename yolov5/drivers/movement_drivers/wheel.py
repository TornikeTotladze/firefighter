from abc import ABC, abstractmethod


class Wheel(ABC):

	@abstractmethod
	def forward(self, step) -> None:
		pass


	@abstractmethod
	def backward(self, step) -> None:
		pass
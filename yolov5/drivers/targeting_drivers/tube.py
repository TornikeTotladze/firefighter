from abc import ABC, abstractmethod


class Tube(ABC):

	@abstractmethod
	def write_angle(angle: float) -> None:
		pass
from abc import ABC, abstractmethod


class Tube(ABC):

	@abstractmethod
	def write_angle(self, angle: float) -> None:
		pass

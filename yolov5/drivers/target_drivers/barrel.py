from abc import ABC, abstractmethod


class Barrel(ABC):

	@abstractmethod
	def write_angle(angle: float) -> None:
		pass
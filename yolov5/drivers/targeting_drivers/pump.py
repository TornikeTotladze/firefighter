from abc import ABC, abstractmethod


class Pump(ABC):

	@abstractmethod
	def inject(self, duration_in_ms: int) -> None:
		pass
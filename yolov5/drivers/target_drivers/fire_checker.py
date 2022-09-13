from abc import ABC, abstractmethod


class FireChecker(ABC):

	@abstractmethod
	def firePresented(self) -> bool:
		pass
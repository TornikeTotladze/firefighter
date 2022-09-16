from abc import ABC, abstractmethod
# from business.listener_api.observer import Observer
from business.dto.target_dto import TargetDto


class Observable(ABC):
	
	@abstractmethod
	def attach(self, observer) -> None:
		pass
			

	@abstractmethod
	def detach(self, observer) -> None:
		pass


	@abstractmethod
	def notify(self) -> None:
		pass


	@abstractmethod
	def get_target_dto(self) -> TargetDto:
		pass


	@abstractmethod
	def set_target_dto(self, target: TargetDto) -> None:
		pass

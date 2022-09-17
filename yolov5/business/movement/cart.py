from abc import ABC, abstractmethod
from business.dto.target_dto import TargetDto
from business.listener_api.observer import Observer
from business.listener_api.observable import Observable


class Cart(ABC):
	
	@abstractmethod
	def move_to_target(target_dto: TargetDto) -> None:
		pass
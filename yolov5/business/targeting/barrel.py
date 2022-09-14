from abc import ABC, abstractmethod
from business.dto.target_dto import TargetDto


class Barrel(ABC):
	
	@abstractmethod
	def stand_on_corresponding_angle(targetDto: TargetDto):
		pass
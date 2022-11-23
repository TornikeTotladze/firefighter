from abc import ABC, abstractmethod


class ObstacleDetector(ABC):

	@abstractmethod
	def distance_to_obstacle(self) -> float:
		pass

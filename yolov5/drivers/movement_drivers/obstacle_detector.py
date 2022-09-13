from abc import ABC, abstractmethod


class ObstacleDetector(ABC):

	@abstractmethod
	def distanceToObstacle(self) -> float:
		pass
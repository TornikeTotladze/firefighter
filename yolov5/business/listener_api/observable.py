from ast import List
from business.listener_api.observer import Observer
from business.dto.target_dto import TargetDto


class Observable():

	target: TargetDto
	update_func: None
	_observers: List[Observer]


	def __init__(self, update: None) -> None:
		self._observers = []
		self.target = None
		self.update_func: None = update

	
	def attach(self, observer: Observer) -> None:
		self._observers.append(observer)
			

	def detach(self, observer: Observer) -> None:
		self._observers.remove(observer)


	def notify(self) -> None:
		for observer in self._observers:
			observer.update(self)

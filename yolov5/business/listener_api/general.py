from ast import List
from business.listener_api.observer import Observer
from business.listener_api.observable import Observable


class General(Observer, Observable):
	
	_observers: List[Observer]


	def __init__(self, update: None) -> None:
		self._observers = []
		self.update_func: None = update

	
	def attach(self, observer: Observer) -> None:
		self._observers.append(observer)
			

	def detach(self, observer: Observer) -> None:
		self._observers.remove(observer)


	def notify(self) -> None:
		for observer in self._observers:
			observer.update(self)

	
	def update(self, observable: Observable):
		self.update_func(observable)
		self.notify()

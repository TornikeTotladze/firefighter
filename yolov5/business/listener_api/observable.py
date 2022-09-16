from ast import List
from business.listener_api.observer import Observer
from business.dto.target_dto import TargetDto


class Observable():

	def __init__(self) -> None:
		self.__observers = []
		self.__target = None

	
	def attach(self, observer: Observer) -> None:
		self.__observers.append(observer)
			

	def detach(self, observer: Observer) -> None:
		self.__observers.remove(observer)


	def notify(self) -> None:
		for observer in self.__observers:
			observer.update(self)

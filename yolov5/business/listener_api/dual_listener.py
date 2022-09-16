from business.listener_api.observer import Observer
from business.listener_api.observable import Observable
from business.listener_api.general_observable import GeneralObservable


class DualListener(Observer, GeneralObservable):
	
	def __init__(self, update_func: None) -> None:
		GeneralObservable.__init__()
		self.__update_func = update_func
		pass


	def update(self, observable: Observable) -> None:
		self.__update_func(observable.get_target_dto())
		self.notify()

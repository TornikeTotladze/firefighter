from ast import List
from business.listener_api.observer import Observer
from business.listener_api.observable import Observable


class General(Observer, Observable):
	
	def update(self, observable: Observable):
		self.update_func(observable)
		self.notify()

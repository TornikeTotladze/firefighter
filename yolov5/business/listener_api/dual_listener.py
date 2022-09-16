from business.listener_api.observable import Observable
from business.listener_api.general_observer import GeneralObserver
from business.listener_api.general_observable import GeneralObservable


class DualListener(GeneralObserver, GeneralObservable):
	
	def __init__(self, update_func: None) -> None:
		GeneralObservable.__init__(self)
		GeneralObserver.__init__(self, update_func)
		pass


	def update(self, observable: Observable) -> None:
		self.set_target_dto(observable.get_target_dto())
		GeneralObserver.update(self, observable)
		self.notify()

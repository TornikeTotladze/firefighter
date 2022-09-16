from business.listener_api.observable import Observable
from business.listener_api.observer import Observer


class GeneralObserver(Observer):

    def __init__(self, update_func: None) -> None:
        self.__update_func = update_func


    def update(self, observable: Observable) -> None:
        self.__update_func(observable.get_target_dto())
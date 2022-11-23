from business.listener_api.observable import Observable
from business.listener_api.observer import Observer
from business.dto.target_dto import TargetDto


class GeneralObservable(Observable):

    def __init__(self) -> None:
        self.__observers = []
        self.target = None

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)

    def get_target_dto(self) -> TargetDto:
        return self.target

    def set_target_dto(self, target: TargetDto) -> None:
        self.target = target

import sys

sys.path.append('../yolov5')

from typing import List
from observables.observable import Observable
from observers.observer import Observer


class CameraDetector(Observable):
    _observers: List[Observer] = []

    def __init__(self) -> None:
        pass

    def attach(self, observer: Observer) -> None :
        self._observers.append(observer) 

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("camera detectori var da cameram mitxra!  " + str(self.probability))
        for obse in self._observers:
            obse.update(self)

    def update(self, c1, c2, center_point, probability):
        self.c1 = c1
        self.c2 = c2
        self.center_point = center_point
        self.probability = probability
        self.notify()


# camera = CameraDetector()
# camera.find_fire()


    
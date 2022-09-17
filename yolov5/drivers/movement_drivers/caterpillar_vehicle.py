import threading

from drivers.movement_drivers.caterpillar import Caterpillar
from drivers.movement_drivers.vehicle import Vehicle
from drivers.movement_drivers.wheel import Wheel


left_en_gpio = 14
left_in1_gpio = 18
left_in2_gpio = 15

right_en_gpio = 23
right_in1_gpio = 17
right_in2_gpio = 27

class CaterpillarVehicle(Vehicle):	
    
    def __init__(self) -> None:
        self.__right_wheel = Caterpillar(en = right_en_gpio, in1 = right_in1_gpio, in2 = right_in2_gpio)
        self.__left_wheel: Wheel = Caterpillar(en = left_en_gpio, in1 = left_in1_gpio, in2 = left_in2_gpio)


    def forward(self, distance: float):
        coef = 1
        step = coef * distance
        self.__move(dir1 = self.__right_wheel.forward, dir2 = self.__left_wheel.forward, step = step)


    def backward(self, distance: float):
        coef = 1
        step = coef * distance
        self.__move(dir1 = self.__right_wheel.backward, dir2 = self.__left_wheel.backward, step = step)


    def turn_right(self, angle: float):
        coef = 4.22
        step = coef * angle
        self.__move(dir1 = self.__right_wheel.backward, dir2 = self.__left_wheel.forward, step = step)


    def turn_left(self, angle: float):
        coef = 4
        step = coef * angle
        self.__move(dir1 = self.__right_wheel.forward, dir2 = self.__left_wheel.backward, step = step)


    def __move(self, dir1: None, dir2: None, step: float):
        th1 = threading.Thread(target = dir1, args = (step,))
        th2 = threading.Thread(target = dir2, args = (0.9*step,))

        th1.start()
        th2.start()
        th1.join()
        th2.join()
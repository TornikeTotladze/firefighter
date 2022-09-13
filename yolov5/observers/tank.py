import threading
from observers.utils.caterpillar import Caterpillar
from observables.observable import Observable
from observers.observer import Observer

right_in1_gpio = 18
right_in2_gpio = 15
right_en_gpio = 23

left_in1_gpio = 17
left_in2_gpio = 27
left_en_gpio = 10

class Tank(Observer):

    def __init__(self) -> None:
        self.right_caterpillar = Caterpillar(en = right_en_gpio, in1 = right_in1_gpio, in2 = right_in2_gpio)
        self.left_caterpillar = Caterpillar(en = left_en_gpio, in1 = left_in1_gpio, in2 = left_in2_gpio)


    def forward(self, distance):
        coef = 1
        step = coef * distance
        self.__move(dir1 = self.right_caterpillar.forward, dir2 = self.left_caterpillar.forward, step = step)


    def backward(self, distance):
        coef = 1
        step = coef * distance
        self.__move(dir1 = self.right_caterpillar.backward, dir2 = self.left_caterpillar.backward, step = step)


    def turn_right(self, degree):
        coef = 1
        step = coef * degree
        self.__move(dir1 = self.right_caterpillar.backward, dir2 = self.left_caterpillar.forward, step = step)


    def turn_left(self, degree):
        coef = 1
        step = coef * degree
        self.__move(dir1 = self.right_caterpillar.forward, dir2 = self.left_caterpillar.backward, step = step)


    def __move(self, dir1, dir2, step):
        th1 = threading.Thread(target = dir1, args = (step,))
        th2 = threading.Thread(target = dir2, args = (step,))

        th1.start()
        th2.start()
        th1.join()
        th2.join()

    def update(self, observable: Observable):
        print("davinaxe yleo xoo")
        self.forward(500)


# tank = Tank()

# tank.forward(23)
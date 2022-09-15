import RPi.GPIO as GPIO
import time
from drivers.movement_drivers.wheel import Wheel


class Caterpillar(Wheel):

    _en: int = None
    _in1: int = None
    _in2: int = None


    def __init__(self, in1: int, in2: int, en: int) -> None:
        self._in1 = in1
        self._in2 = in2
        self._en = en

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._in1 ,GPIO.OUT)
        GPIO.setup(self._in2,GPIO.OUT)
        GPIO.setup(self._en,GPIO.OUT)
        
        GPIO.output(self._in1 ,GPIO.LOW)
        GPIO.output(self._in2 ,GPIO.LOW)
        self.p = GPIO.PWM(self.en ,1000)
        self.p.start(100)


    def forward(self, step: int):
        t = 0
        GPIO.output(self._in1,GPIO.LOW)
        GPIO.output(self._in2,GPIO.HIGH)

        while t < step:
            time.sleep(0.001)
            t += 1

        GPIO.output(self._in2,GPIO.LOW)


    def backward(self, step: int):
        t = 0
        GPIO.output(self._in1,GPIO.HIGH)
        GPIO.output(self._in2,GPIO.LOW)

        while t < step:
            time.sleep(0.001)
            t += 1

        GPIO.output(self._in1,GPIO.LOW)


 
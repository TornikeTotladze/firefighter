from ctypes.wintypes import BOOL
from typing import List
import RPi.GPIO as GPIO
import time
from observable import Observable
from observer import Observer
from tank import Tank


class FlameDetector():

    _observers: List[Observer] = []

    def __init__(self) -> None:
        self.pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def check_flame(self) -> BOOL:
        read = GPIO.input(self.pin)
        return read == GPIO.LOW

    



#######################################################







detector = FlameDetector()

tank = Tank()

detector.attach(tank)


while True:
    time.sleep(1) 
    if detector.check_flame():
        detector.notify()  
    
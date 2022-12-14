import RPi.GPIO as GPIO

from drivers.targeting_drivers.fire_checker import FireChecker


class FlameSensor(FireChecker):

    def __init__(self, pin: int) -> None:
        self.__pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pin, GPIO.IN)

    def fire_presented(self) -> bool:
        read = GPIO.input(self.__pin)
        return read == GPIO.LOW

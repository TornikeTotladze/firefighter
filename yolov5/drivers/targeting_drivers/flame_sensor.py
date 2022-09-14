import RPi.GPIO as GPIO

from drivers.target_drivers.fire_checker import FireChecker


class FlameSensor(FireChecker):

	def __init__(self, pin: int) -> None:
		self.pin = pin
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.IN)


	def firePresented(self) -> bool:
		read = GPIO.input(self.pin)
		return read == GPIO.LOW
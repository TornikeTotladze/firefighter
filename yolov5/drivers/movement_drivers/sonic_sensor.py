import RPi.GPIO as GPIO
import time

from drivers.movement_drivers.obstacle_detector import ObstacleDetector


class SonicSensor(ObstacleDetector):

	def __init__(self, trig_pin: int, echo_pin: int) -> None:
		self.trigger = trig_pin
		self.echo = echo_pin

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.trigger, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)


	def distanceToObstacle(self) -> float:
		GPIO.output(self.trigger, True)
 
		time.sleep(0.00001)
		GPIO.output(self.trigger, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(self.echo) == 0:
			StartTime = time.time()

		while GPIO.input(self.echo) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime
		distance = (TimeElapsed * 34300) / 2

		return distance

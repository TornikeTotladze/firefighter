import RPi.GPIO as GPIO
import time

from drivers.movement_drivers.obstacle_detector import ObstacleDetector


class SonicSensor(ObstacleDetector):

	def __init__(self, trig_pin: int, echo_pin: int) -> None:
		self.__trigger = trig_pin
		self.__echo = echo_pin

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__trigger, GPIO.OUT)
		GPIO.setup(self.__echo, GPIO.IN)


	def distanceToObstacle(self) -> float:
		GPIO.output(self.__trigger, True)
 
		time.sleep(0.00001)
		GPIO.output(self.__trigger, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(self.__echo) == 0:
			StartTime = time.time()

		while GPIO.input(self.__echo) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime
		distance = (TimeElapsed * 34300) / 2

		return distance

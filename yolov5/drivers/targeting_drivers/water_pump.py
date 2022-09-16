import time
import RPi.GPIO as GPIO

from drivers.targeting_drivers.pump import Pump


class WaterPump(Pump):

	def __init__(self, in1: int, in2: int, en: int) -> None:
		self.__in1 = in1
		self.__in2 = in2
		self.__en = en

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__in1 ,GPIO.OUT)
		GPIO.setup(self.__in2,GPIO.OUT)
		GPIO.setup(self.__en,GPIO.OUT)
		
		GPIO.output(self.__in1 ,GPIO.LOW)
		GPIO.output(self.__in2 ,GPIO.LOW)
		self.p = GPIO.PWM(self.__en ,1000)
		self.p.start(100)


	def inject(self, duration_in_ms: int) -> None:
		t = 0
		GPIO.output(self.__in1,GPIO.LOW)
		GPIO.output(self.__in2,GPIO.HIGH)

		while t < duration_in_ms:
			time.sleep(0.001)
			t += 1

		GPIO.output(self.__in2,GPIO.LOW)

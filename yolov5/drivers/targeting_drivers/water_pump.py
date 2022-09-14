import time
import RPi.GPIO as GPIO

from drivers.targeting_drivers.pump import Pump


class WaterPump(Pump):

	def __init__(self, in1: int, in2: int, en: int) -> None:
		self.in1 = in1
		self.in2 = in2
		self.en = en

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.in1 ,GPIO.OUT)
		GPIO.setup(self.in2,GPIO.OUT)
		GPIO.setup(self.en,GPIO.OUT)
		
		GPIO.output(self.in1 ,GPIO.LOW)
		GPIO.output(self.in2 ,GPIO.LOW)
		self.p = GPIO.PWM(self.en ,1000)
		self.p.start(100)


	def inject(self, duration_in_ms: int) -> None:
		t = 0
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.HIGH)

		while t < duration_in_ms:
			time.sleep(0.001)
			t += 1

		GPIO.output(self.in2,GPIO.LOW)

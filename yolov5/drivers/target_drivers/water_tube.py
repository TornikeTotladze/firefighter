import math

from drivers.target_drivers.barrel import Barrel
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory


servo_pwm_pin = 12
servo_min_pw = 0.9/1000
servo_max_pw = 2/1000

servo_min_angle = -91
servo_max_angle = 91

class WaterTube(Barrel):

	def __init__(self) -> None:
		self.factory = PiGPIOFactory()
		self.servo = Servo(servo_pwm_pin, pin_factory=self.factory, min_pulse_width=servo_min_pw, max_pulse_width=servo_max_pw)


	def write_angle(self, angle: float) -> None:
		if angle not in range(servo_min_angle, servo_max_angle):
			raise ValueError("angle must be in the range(" + str(servo_min_angle) + ", " + str(servo_max_angle) + ")!")
		self.servo.value = math.sin(math.radians(angle))

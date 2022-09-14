# from time import sleep
# from observers.barrel import Barrel
# from observers.tank import Tank

# barrel = Barrel()

# for i in range(-80, -40):
#     barrel.write_angle(i)
#     sleep(0.05)

# tank = Tank()

# tank.forward(1000)
# barrel.write_angle(-40)

from asyncio import sleep
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle
from drivers.movement_drivers.vehicle import Vehicle
from drivers.targeting_drivers.tube import Tube
from drivers.targeting_drivers.fire_checker import FireChecker
from drivers.targeting_drivers.flame_sensor import FlameSensor
from drivers.targeting_drivers.pump import Pump
from drivers.targeting_drivers.water_pump import WaterPump
from drivers.targeting_drivers.water_tube import WaterTube
from drivers.movement_drivers.obstacle_detector import ObstacleDetector
from drivers.movement_drivers.sonic_sensor import SonicSensor

barel: Tube = WaterTube()

barel.write_angle(-60);
# sleep(1000)
# barel.write_angle(30)

pump: Pump = WaterPump(10, 9, 22)

pump.inject(7000)

fire_checker: FireChecker = FlameSensor(20)

# while 1:
#     if fire_checker.firePresented():
#         print("fire")


vehicle: Vehicle = CaterpillarVehicle()

vehicle.forward(200)

sleep(1)

vehicle.backward(200)

sleep(1)

vehicle.turn_right(500)

sleep(1)

vehicle.turn_left(900)


right_sonic: ObstacleDetector = SonicSensor(7, 8)
left_sonic: ObstacleDetector = SonicSensor(25, 24)

print("left: " + str(left_sonic.distanceToObstacle()))
print("right: " + str(right_sonic.distanceToObstacle()))
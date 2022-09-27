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

# from asyncio import sleep
# from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle
# from drivers.movement_drivers.vehicle import Vehicle
# from drivers.targeting_drivers.tube import Tube
# from drivers.targeting_drivers.fire_checker import FireChecker
# from drivers.targeting_drivers.flame_sensor import FlameSensor
# from drivers.targeting_drivers.pump import Pump
# from drivers.targeting_drivers.water_pump import WaterPump
# from drivers.targeting_drivers.water_tube import WaterTube
# from drivers.movement_drivers.obstacle_detector import ObstacleDetector
# from drivers.movement_drivers.sonic_sensor import SonicSensor

# barel: Tube = WaterTube()

# barel.write_angle(-60);
# # sleep(1000)
# # barel.write_angle(30)

# pump: Pump = WaterPump(10, 9, 22)

# pump.inject(7000)

# fire_checker: FireChecker = FlameSensor(20)

# # while 1:
# #     if fire_checker.firePresented():
# #         print("fire")


# vehicle: Vehicle = CaterpillarVehicle()

# vehicle.forward(200)

# sleep(1)

# vehicle.backward(200)

# sleep(1)

# vehicle.turn_right(500)

# sleep(1)

# vehicle.turn_left(900)


# right_sonic: ObstacleDetector = SonicSensor(7, 8)
# left_sonic: ObstacleDetector = SonicSensor(25, 24)

# print("left: " + str(left_sonic.distanceToObstacle()))
# print("right: " + str(right_sonic.distanceToObstacle()))

from time import sleep
from business.dto.target_dto import TargetDto
from business.listener_api.general_observable import GeneralObservable
from business.listener_api.general_observer import GeneralObserver
from business.targeting.target_discoverer import TargetDiscoverer
from business.listener_api.dual_listener import DualListener
from drivers.movement_drivers.caterpillar_vehicle import CaterpillarVehicle
from drivers.movement_drivers.vehicle import Vehicle
from drivers.targeting_drivers.pump import Pump
from drivers.targeting_drivers.water_pump import WaterPump
from business.movement.cart import Cart
from business.movement.tank import Tank
from business.targeting.barrel import Barrel
from business.targeting.water_jet_barrel import WaterJetBarrel
from business.extinguishing.fire_extinguisher import FireExtinguisher
from business.extinguishing.water_jet_fire_extinguisher import WaterJetFireExtinguisher
from business.dto.fire_dto import FireDto
from drivers.targeting_drivers.water_tube import WaterTube



# car: Vehicle = CaterpillarVehicle()
# car.turn_left(360)
# sleep(1)
# car.turn_right(380)
# cart: Cart = Tank()
# barrel: Barrel = WaterJetBarrel()
# fire_extinguisher: FireExtinguisher = WaterJetFireExtinguisher()

# camera = TargetDiscoverer()
# tank = DualListener(cart.move_to_target)
# targeter = DualListener(barrel.stand_on_corresponding_angle)
# pump = GeneralObserver(fire_extinguisher.extinguish)


# targeter.attach(pump)
# tank.attach(targeter)
# camera.attach(tank)


# target_dto: TargetDto = FireDto("fire")
# camera.set_target_dto(target_dto)
# camera.notify()


# pump: Pump = WaterPump(10, 9, 22)

# pump.inject(100000)

tube = WaterTube()

tube.write_angle(-45)


# fire_extinguisher.extinguish(50000)
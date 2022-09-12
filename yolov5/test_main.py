from time import sleep
from observers.barrel import Barrel
from observers.tank import Tank

barrel = Barrel()

for i in range(-80, -40):
    barrel.write_angle(i)
    sleep(0.05)

tank = Tank()

tank.forward(1000)

    # barrel.write_angle(-40)
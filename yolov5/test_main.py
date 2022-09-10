from time import sleep
from observers.barrel import Barrel

barrel = Barrel()

for i in range(-80, -40):
    barrel.write_angle(i)
    sleep(0.05)

    # barrel.write_angle(-40)
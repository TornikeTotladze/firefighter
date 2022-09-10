
import threading
from time import sleep
from observers.tank import Tank


# def main(opt):
#     # Gen.check_requirements(exclude=('tensorboard', 'thop'))
#     # detect.run(weights="best.pt", source=0)
#     caterpillar1 = Caterpillar()
#     caterpillar1.forward(10)


# if __name__ == "__main__":
#     opt = detect.parse_opt()
#     main(opt)

# caterpillar1 = Caterpillar()
# caterpillar1.forward(10)

# caterpillar1 = Caterpillar(in1=24, in2=23, en=25)
# caterpillar2 = Caterpillar(in1=27, in2=22, en=4)
# # caterpillar1.forward(1000)
# # caterpillar2.forward(1000)
# th1 = threading.Thread(target=caterpillar1.forward, args=(5000,))
# th2 = threading.Thread(target=caterpillar2.backward, args=(5000,))

# th1.start()
# th2.start()
# print(threading.active_count())
# th1.join()
# th2.join()
# print(threading.active_count())

tank = Tank()
while True:
    tank.forward(500)
    sleep(1)
    # tank.forward(500)
    # sleep(0.2)
    # tank.forward(500)
    # sleep(0.2)
    tank.backward(500)
    sleep(1)


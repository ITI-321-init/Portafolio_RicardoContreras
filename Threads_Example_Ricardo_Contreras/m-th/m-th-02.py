#      Threading program
#         Objetive: Running 3 different tasks via threading
#         You are running late for school, and you need to finish 3 task to get ready

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you ate Breakfast")


def take_shower():
    time.sleep(4)
    print("you took a shower")


def take_bus():
    time.sleep(5)
    print("you took the bus")

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=take_shower)
y.start()

z = threading.Thread(target=take_bus)
z.start()

x.join()
y.join()
z.join()




print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


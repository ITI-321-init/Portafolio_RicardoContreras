#   threads that runs on the background, can be used as background tasks such as garbage collection, waiting for input
#    or long-running processes


import threading
import time



def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('Logged in for,', count, 'seconds')


x = threading.Thread(target=timer, daemon=True)
x.start()

#x.setDaemon(True)



answer = input('Wanna exit? (y/n) ')

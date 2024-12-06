# multithreading fundamentals

import threading
import time
def walk_dog(first):
    time.sleep(8)
    print(f'you finish walking {first}')

def take_out_trash(message1, first):
    time.sleep(2)
    print(f'you take out trash {message1}, {first}')

def get_mail():
    time.sleep(4)
    print('you got the mail')

# If working with one parameter, need to add a ',' at the end like so:
chore1 = threading.Thread(target=walk_dog, args=('Wisky',))
chore1.start()

# if working with more than 1 parameter, no need to end with ',' like so:
chore2 = threading.Thread(target=take_out_trash, args=('good job', 'Ricardo'))
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('all chores are complete!')
print(time.perf_counter())



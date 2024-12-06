import time

print(time.ctime())

print(time.time())


print(time.ctime(time.time()))


time_object = time.localtime()

print(time_object)

local_time = time.strftime('%B %d %Y %H:%M:%S', time_object)
print(local_time)

time_string = '20 April 2024'
time_object = time.strptime(time_string, '%d %B %Y')
print(time_object)


time_tuple = (2024, 4, 20, 4 ,20, 0, 0, 0, 0)

time_string = time.asctime(time_tuple)
print(time_string)


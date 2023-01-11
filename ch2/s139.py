import time

current_time = time.time()

second = int(current_time) % 60
minute = int(current_time / 60) % 60
hour = int((current_time / 60) / 60) % 24


print("Current time:", str(hour) + ":" + str(minute) + ":" + str(second), "GMT")

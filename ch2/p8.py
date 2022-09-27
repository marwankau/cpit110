import time
current_time = time.time()  # give current time

second = round(current_time) % 60
minute = (round(current_time) // 60) % 60
hour = (round(current_time) // (60 * 60)) % 24  # or 3600
#     convert to min     to hour     to days
day = (((current_time // 60) // 60) // 24) // 365 + 1970
# day = current_time // (60 * 60 * 24)  # short form


gmt = str(day) + ", " + str(hour) + ":" + str(minute) + ":" + str(second) + " GMT"

print("current time is", gmt)

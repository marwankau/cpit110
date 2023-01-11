kilometers = 14
minutes = 45
seconds = 30

ONE_MILE_AS_KILO = 1.6

miles = kilometers / ONE_MILE_AS_KILO

hours = minutes / 60 + seconds / (60 * 60)

avg_speed = miles / hours
print("Average speed is", avg_speed, " m/h")

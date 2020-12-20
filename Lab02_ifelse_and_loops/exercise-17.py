
#This program converts KPH to MPH.

#constant
CONVERT_FACTOR = 0.6214

#head output
print("KPH \t MPH")
print("_" * 20)

#loop
for kph_speed in range (60, 131, 10):

    #calculation
    mph_speed = kph_speed * CONVERT_FACTOR

    #output
    print(kph_speed, '\t', format(mph_speed, '.1f'))

input("\nPress any key to quit")

# Case 1
# KPH      MPH
# ____________________
# 60       37.3
# 70       43.5
# 80       49.7
# 90       55.9
# 100      62.1
# 110      68.4
# 120      74.6
# 130      80.8

# Press any key to quit
# Problem: Given a radius, print the area and circumference to two decimals.

import math

radius = float(input("Enter radius : "))
pi = math.pi

area = pi * radius**2
circumference = 2 * pi * radius

print(f"Area : {area:.2f}")
print(f"Circumference : {circumference:.2f}")

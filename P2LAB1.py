# Samari Franklin
# 9/11/2024
# P2LAB1
# This program will calculate the diameter, circumference, and area of a circle.

# import math library 
import math

radians = float(input("What is the radius of the circle? "))
diameter = radians * 2
# calculate the circum
circum = 2  * math.pi * radians
# calculate the area
area = math.pi * (radians ** 2)
print()
print(radians)
print()
print("The diameter of the circle is", diameter)
print()
print("The circumference of the circle is" , round(circum, 2))
print()
print("the area of the circle is", round(area, 3))
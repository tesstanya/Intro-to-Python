# This program finds the area of a pentagon

import math

radius = eval(input("Enter the length from the center to a vertex: "))

side = 2 * radius * math.sin(math.pi / 5)

area = (3 * math.sqrt(3) * side ** 2) / 2

print("The area of the pentagon is ", area)
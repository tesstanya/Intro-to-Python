# This program computes the volume of a cylinder
radius, length = eval(input("Enter the radius and length of a cylinder: "))
area = radius * radius * 3.14
print("The area is", area)
volume = area * length
print("The volume is", volume)
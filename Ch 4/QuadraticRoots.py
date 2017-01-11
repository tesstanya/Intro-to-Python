import math

a, b, c = eval(input("Enter a, b, c: "))

discriminant = b * b - 4 * a * c

if discriminant < 0:
	print("The equation has no real roots")
elif discriminant == 0:
	r1 = (-b + math.sqrt(b * b - 4 * a * c))/(2 * a)
	print("The root is", r1)
elif discriminant > 0:
	r1 = (-b + math.sqrt(b * b - 4 * a * c))/(2 * a)
	r2 = (-b - math.sqrt(b * b - 4 * a * c))/(2 * a)
	print("The roots are", r1, "and", r2)


# This program takes an integer between
# 0 to 15 and prints the hex value of it

value = eval(input("Enter a decimal value (0-15): "))

if value < 0 or value > 15:
	print("Invalid input")
else:
	# format prints the value without 0x in front
	print("The hex value is", format(value, "X"))
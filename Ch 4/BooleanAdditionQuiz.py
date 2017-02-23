import random

num1 = random.randrange(0,100) #randrange is one less than the max (0-99)
num2 = random.randint(0,99) #randint includes the max (0-99)

answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

if answer == (num1 + num2):
	print("True")
else:
	print("False")
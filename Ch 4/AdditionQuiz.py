import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)

# Need to convert nums to string for the eval statement (input is string only)
answer = eval(input("What is " + str(num1) + " + " + str(num2) + " + " 
+ str(num3) + " ? "))

addnums = num1 + num2 + num3

if addnums == answer:
	print("Your answer is correct!")
else:
	print("Wrong! The correct answer is", addnums)
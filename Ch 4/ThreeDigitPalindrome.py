# This program checks if the user
# input for a three digit integer
# is a palindrome

num = eval(input("Enter a three-digit integer: "))

# get the hundreths digit and the ones digit
if num // 100 == num % 10:
	print(num, "is a palindrome")
else:
	print(num, "is not a palindrome")
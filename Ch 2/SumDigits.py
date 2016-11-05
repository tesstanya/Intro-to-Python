# Find the sum of an integer's digits

number = eval(input("Enter a number between 0 and 1000: "))
digit1 = number % 10 # get the digit in the ones place
number = number // 10 # eliminate the digit in the ones place
digit2 = number % 10
digit3 = number // 10

sum = digit1 + digit2 + digit3

print("The sum of digits is", sum)
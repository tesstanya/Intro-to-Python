# Reverse a 4-digit number manually

num = eval(input("Enter a 4-digit number: "))

digit1 = num % 10

num //= 10

digit2 = num % 10

num //= 10

digit3 = num % 10

digit4 = num // 10

reverse = digit1 * 1000 + digit2 * 100 + digit3 * 10 + digit4

print("The reversed number is:", reverse)
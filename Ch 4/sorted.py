# This program uses conditional expression
# to assign a value to a variable depending
# on the result of the condition

x,y,z = eval(input("Enter three numbers (separated by commas): "))
print("numbers are sorted" if x < y and y < z else "numbers are not sorted")
# This program compares the cost
# of two packages and prints
# the package with the best rate

weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

pack1 = weight1 / price1
pack2 = weight2 / price2

print("Package 1 has the better price" if pack1 < pack2 else "Package 2 has the better price")
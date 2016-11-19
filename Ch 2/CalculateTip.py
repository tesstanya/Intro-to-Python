# Calculate tip
subtotal, gratituity = eval(input("Enter the subtotal and a gratituity rate: "))
tip = subtotal * (gratituity/100)
total = subtotal + tip
print("The gratituity is", gratituity, "and the total is", format(total, ".2f"))
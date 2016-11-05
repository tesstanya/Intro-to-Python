# Investment amount
finalAccountValue = eval(input("Enter final account value: "))
monthlyInterestRate = eval(input("Enter annual interest rate in percent: ")) / (12 * 100)
numberOfMonths = eval(input("Enter number of years: ")) * 12
initalDepositAmount = finalAccountValue / (1 + monthlyInterestRate)**numberOfMonths
print("Initial deposit value is", initalDepositAmount)

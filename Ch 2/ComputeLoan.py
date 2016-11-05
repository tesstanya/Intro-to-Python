# Enter annual interest rate as percentage eg. 7.25
annualInterestRate = eval(input("Enter annual interest rate, ex. 7.25: "))
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = eval(input("Enter number of years as an integer: "))

# Enter loan amount
loanAmount = eval(input("Enter loan amount: "))

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is", int(monthlyPayment * 100) / 100 )
print("The total payment is", int(totalPayment * 100) / 100 )
import sys

day = eval(input("Enter today's day: "))

if day > 6:
	print("Invalid day")
	sys.exit()

if day == 0:
	today = "Sunday"
elif day == 1:
	today = "Monday"
elif day == 2:
	today = "Tuesday"
elif day == 3:
	today = "Wednesday"
elif day == 4:
	today = "Thursday"
elif day == 5:
	today = "Friday"
elif day == 6:
	today = "Saturday"

num = eval(input("Enter the number of days elapsed since today: "))

future = (day + num) % 7

if future == 0:
	fday = "Sunday"
elif future == 1:
	fday = "Monday"
elif future == 2:
	fday = "Tuesday"
elif future == 3:
	fday = "Wednesday"
elif future == 4:
	fday = "Thursday"
elif future == 5:
	fday = "Friday"
elif future == 6:
	fday = "Saturday"

print("Today is " + today + " and the future day is " + fday)
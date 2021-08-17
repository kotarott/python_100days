age = input("What is your current age? >>> ")

# write your code below
age_as_int = int(age)
years_remaining = 90 - age_as_int

days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
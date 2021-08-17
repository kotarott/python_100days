height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# write your code below this line
bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    message = f"Your BMI is {bmi}, you are underweight."
elif bmi < 25:
    message = f"Your BMI is {bmi}, you have a normal weight."
elif bmi < 30:
    message = f"Your BMI is {bmi}, you are slightly overweight."
elif bmi < 35:
    message = f"Your BMI is {bmi}, you are obese."
else:
    message = f"Your BMI is {bmi}, you are clinically obese."

print(message)


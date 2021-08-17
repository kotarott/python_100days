print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n>>> $")
tip_percentage = input("What percentage tip would like to give? 10, 12, or 15?\n>>> ")
number_of_people = input("How many people to split the bill?\n>>> ")

float_bill = round(float(bill), 2)
float_tip_percentage = (100 + int(tip_percentage)) / 100
int_number_of_people = int(number_of_people)

bill_per_person = round((float_bill / int_number_of_people) * float_tip_percentage, 2)

message = "Each person should pay ${:.2f}".format(bill_per_person)
print(message)
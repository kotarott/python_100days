year = int(input("Which year do you want to check? "))

# write your code below this line
split_by_4 = year % 4
split_by_100 = year % 100
split_by_400 = year % 400

if split_by_4 == 0:
    message = "Leap year."
    if split_by_100 == 0:
        message = "Not leap year."
        if split_by_400 == 0:
            message = "Leap year."
else:
    message = "Not leap year."

print(message)
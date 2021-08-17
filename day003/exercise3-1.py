number = int(input("Which number do you want to check?\n>>> "))

split_amount = number % 2

if split_amount == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
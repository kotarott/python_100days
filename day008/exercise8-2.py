# Write your code below this line
def prime_checker(number):
    i = 2
    while i < number:
        if number % i == 0:
            return "It's not a prime number."
        else:
            i += 1
    return "It's a prime number."


n = int(input("Check this number: "))
print(prime_checker(number=n))
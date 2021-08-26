name_string = input("Give me everybody's names, separated by a comma. >>> ")
names = name_string.split(", ")

import random

random_name = random.randint(0, len(names)-1)
# person_who_will_pay_bill = names[random_name]

person_who_will_pay_bill = random.choice(names)
print(f"{person_who_will_pay_bill} is going to buy the meal today!!")
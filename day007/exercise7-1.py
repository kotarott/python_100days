import random

word = ["aardvark", "baboon" ,"camel"]

chosen_word = random.choice(word)
print(chosen_word)

guess = input("Guess the word. >>> ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
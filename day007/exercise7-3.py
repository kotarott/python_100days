import random


def to_string(values):
    word = ""
    for letter in values:
        word += letter
    return word


word = ["aardvark", "baboon" ,"camel"]
chosen_word = random.choice(word)
word_length = len(chosen_word)

print(f"Pssst, the solution is {chosen_word}")

display = []
for _ in range(word_length):
    display.append("_")

# while chosen_word != to_string(display):

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter. >>> ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

print("Game Over")
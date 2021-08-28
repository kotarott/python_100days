import random

word = ["aardvark", "baboon" ,"camel"]

chosen_word = random.choice(word)

answer = []
for _ in range(len(chosen_word)):
    answer.append("_")
print(answer)

guess = input("Guess the word. >>> ").lower()

for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        answer[position] = guess

# for letter in chosen_word:
#     if letter == guess:
#         answer.append(letter)
#     else:
#         answer.append("_")
print(answer)
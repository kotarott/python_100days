print("Welcome to the Love Caluclator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Write your code below this line
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

# 最初に文字結合して、countした方が少ないコードで済む。

count_true = 0
count_true += name1_lowercase.count("t") + name2_lowercase.count("t")
count_true += name1_lowercase.count("r") + name2_lowercase.count("r")
count_true += name1_lowercase.count("u") + name2_lowercase.count("u")
count_true += name1_lowercase.count("e") + name2_lowercase.count("e")

count_love = 0
count_love += name1_lowercase.count("l") + name2_lowercase.count("l")
count_love += name1_lowercase.count("o") + name2_lowercase.count("o")
count_love += name1_lowercase.count("v") + name2_lowercase.count("v")
count_love += name1_lowercase.count("e") + name2_lowercase.count("e")

love_score = int(str(count_true) + str(count_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, You go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


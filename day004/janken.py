import random

rock = """
グー！　　 ＿_
　　　　　/｣｣｣｣
　　　　 ｜っ丿
　 ∧_∧ / ／
　( ･ω･)／
　(つ　 ﾉ
　 ｕ-ｕ
"""

paper = """
パー！
　　　　　｢｢｢h
　　　　 Ｃ　ﾉ
　 ∧_∧ / ／
　( ･ω･)／
　(つ　 ﾉ
　 ｕ-ｕ
"""

scissors = """
チョキ！
　　　　　(Ｖ)
　　　　　/ｱE)
　 ∧_∧ / ／
　( ･ω･)／
　(つ　 ﾉ
　 ｕ-ｕ
"""
map = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors Game!")
your_hand = int(input("What do you choose? Type 0 for グー, 1 for パー or 2 for チョキ."))

com_hand = random.randint(0, 2)

print(f"You:\n{map[your_hand]}\nCOM:{map[com_hand]}")

if your_hand == 0:
    if com_hand == 2:
        print("You win.")
    elif com_hand == 1:
        print("You lose.")
    else:
        print("Draw")
elif your_hand == 1:
    if com_hand == 0:
        print("You win.")
    elif com_hand == 2:
        print("You lose.")
    else:
        print("Draw")
elif your_hand == 2:
    if com_hand == 1:
        print("You win.")
    elif com_hand == 0:
        print("You lose.")
    else:
        print("Draw")
else:
    print("Error")
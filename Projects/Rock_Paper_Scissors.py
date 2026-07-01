import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [Rock, Paper, Scissors]

choice_names = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")
)

if user_choice not in choice_names:
    print("You typed an invalid number, you lose.")
else:
    print(f"You chose {choice_names[user_choice]}")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print(f"Computer chose {choice_names[computer_choice]}")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")

    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")

    else:
        print("You lose!")
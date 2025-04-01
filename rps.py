import random



rock = '''

  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n ")

try:
    user_choice = int(user_input)
    if not 0 <= user_choice <= 2:
        raise ValueError("Input out of range. Please enter 0, 1, or 2.")
    print(game_images[user_choice])

    comp_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif user_choice > comp_choice:
        print("You win!")
    elif user_choice == comp_choice:
        print("Draw!")
    else:
        print("You lose!")

except ValueError as e:
    print(e)
    exit()

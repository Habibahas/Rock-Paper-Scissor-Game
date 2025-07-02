import random

rock_ascii = """
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" 



paper_ascii = """
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""




scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""



print("Welcome to the Rock, Paper, Scissors game!") 
press = input("Press Enter to continue or type Help for the rules\n").lower()

if press == "help":
    print("""        *****Rules*****
       1) You choose and the computer chooses.
       2) Rock beats Scissors -> Rock wins.
       3) Scissors beats Paper -> Scissors wins.
       4) Paper covers Rock -> Paper wins.""")

user_choice = input("Enter your choice: rock, paper, scissors").lower()

if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose rock, paper, or scissors.")

else:
    if user_choice == "rock":
        print(f"\nyou chose: \n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nyou chose: \n{paper_ascii}")
    else:
        print(f"\nyou chose: \n{scissors_ascii}")
  
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
  print("It's a tie!")

elif ( 
  (user_choice == "rock" and computer_choice == "scissors")
  or (user_choice == "scissors" and computer_choice == "paper")
  or
  (user_choice == "paper" and computer_choice == "rock")
  
):
    print(f"You Win! {user_choice} beats       {computer_choice}")

else:
    print(f"You lose! {computer_choice} beats {user_choice}")

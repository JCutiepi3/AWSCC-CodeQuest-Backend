import random

pos_choice = ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(pos_choice)

print("<Rock, Paper, Scissors>")
player = input("What's your move?")

# checks the possible outcomes
if (player.lower() == "paper" and comp_choice == "Rock") or \
   (player.lower() == "scissors" and comp_choice == "Paper") or \
   (player.lower() == "rock" and comp_choice == "Scissors"):
   print("The computer's move:",comp_choice)
   print("The player wins!!")
         
elif player.lower() == comp_choice.lower():
    print("The computer's move:",comp_choice)
    print("It's a tie!")

else:
    print("The computer's move:", comp_choice)
    print("The computer wins!")

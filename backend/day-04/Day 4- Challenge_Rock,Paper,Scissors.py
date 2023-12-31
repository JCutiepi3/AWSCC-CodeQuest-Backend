import os #imports functions in the operating system

level_1 = "Paper"
level_2 = "Scissors"
level_3 = "Rock"

print("[<Rock>, <Paper>, <Scissors> Game!!]")

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Player 1 input
player1 = input("Player 1, enter your move: ")

# Clear the screen to hide Player 1's move
clear_screen()

# Player 2 input
player2 = input("Player 2, enter your move: ")

# Check the winner
if (player1 == level_1 and player2 == level_3) or \
   (player1 == level_2 and player2 == level_1) or \
   (player1 == level_3 and player2 == level_2):
    print("Player 1 wins!")
elif (player2 == level_1 and player1 == level_3) or \
     (player2 == level_2 and player1 == level_1) or \
     (player2 == level_3 and player1 == level_2):
    print("Player 2 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")

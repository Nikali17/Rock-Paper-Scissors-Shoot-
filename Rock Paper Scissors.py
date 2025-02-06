
import random # Import random allows user to access all functions in the random module

while True: # Creates a while loop as long as users condtion are true loop won't break
 user_action = input("Please pick Rock,Paper,or Scissors or type End to exit the game") # This takes the users action
 actions = ["Rock" , "Paper" , "Scissors"] # Choices the user has in our game of rock paper scissors
 computer_action = random.choice(actions)
 print(f"\nYou Choose {user_action}, Computer Chose {computer_action}.\n");
 if user_action == computer_action:
  print("Its a tie!")
 elif user_action == "Rock":
   if computer_action == "Scissors":
        print("Rock beats Scissors You Win!")
   else:
        print("Paper covers Rock You Lose")
 elif user_action == "Paper":
   if computer_action == "Rock":
        print("You Win!")
   else:
        print("You Lose")
 elif user_action == "Scissors":
   if computer_action == "Paper":
        print("You Win!")
   else:
        print("You Lose!")

 play_again = input("Play again? (y/n): ") # the code here will keep the game running
 if play_again.lower() != "y":
  break
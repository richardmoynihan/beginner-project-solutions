# importing requires random module
import random
while True:
  print("Now please enter your choice no. \n 1. Rock \n 2. Paper \n 3. Scissor \n")
  # input from user
  ch = int(input("Now Your Turn: "))
  while ch> 3 or ch< 1:
     ch = int(input("Enter Your Choice Here: "))
  if ch == 1:
     choice_name = 'Rock'
  elif ch == 2:
     choice_name = 'Paper'
  else:
     choice_name = 'Scissors'
  # print user given choice
  print("Your choice is: " + choice_name)
  print("\nNow its the computer turn....")
  # Computer will select a random number
  # in the range of 1, 2 and 3. Using randint method
  comp_choice = random.randint(1, 3)
  # looping will continue until comp_choice value
  # is equal to the choice value
  while comp_choice == ch:
    comp_choice = random.randint(1,3)
    # choosing value of the variable comp_choice_name
  if comp_choice == 1:
     comp_choice_name = 'Rock'
  elif comp_choice == 2:
     comp_choice_name = 'Paper'
  else:
     comp_choice_name = 'Scissors'
  print("Computer Choice is: " + comp_choice_name)
  print(choice_name + " V/s " + comp_choice_name)
  # condition for winning the game
  if((ch == 1 and comp_choice == 2) or
     (ch == 2 and comp_choice ==1 )):
      print("Paper Wins-> ",end = " ")
      final_result = "Paper"
  elif((ch == 1 and comp_choice == 3) or
     (ch == 3 and comp_choice == 1)):
    print("Rock Wins ->",end = " ")
    final_result = "Rock"
  else:
     print("Scissor Wins ->",end = " ")
     final_result = "Scissors"
  # Prints if user or computer wins
  if final_result == choice_name:
     print(" You are the Winner ",end = " ")
  else:
     print(" Computer Wins " )
  print("Do you want to play again? (Y/N)")
  ans = input()
      # If user input n or N then condition is True
  if ans == 'n' or ans == 'N':
     break
   # If exiting from the while loop
  print("\nThanks for Playing")

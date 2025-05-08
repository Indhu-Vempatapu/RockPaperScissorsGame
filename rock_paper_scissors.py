# import random module
import random

user_score = 0
comp_score = 0

print('''Winning Rules Of Rock Paper Scissors \n
      Rock vs Paper --> Paper wins
      Rock vs Scissors --> Rock wins
      Paper vs Scissors --> Scissor wins''')
print("\n")
print("Enter your choice")
print("1.Rock")
print("2.Paper")
print("3.Scissor")

while True:

   # prompts the user for input
    user_choice = int(input("Enter your choice :"))

    # looping until user enter invalid input
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Enter a valid choice please : '))

    # initialize value of user_choice_name variable 
    # corressponding to user_choice value
    if user_choice == 1:
        user_choice_name = "Rock"
        print("User choice is Rock")
    elif user_choice == 2:
        user_choice_name = "Paper"
        print("User choice is Paper")
    else:
        user_choice_name = "Scissors"
        print("User choice is Scissor")

    #prints user choice
    print('Now its Computers Turn..')
    print("\n")

    #Computer chooses randomly any number among 3
    comp_choice = random.randint(1, 3)

    #looping until comp_choice value equal to user_choice
    while comp_choice == user_choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    if comp_choice == 1:
        comp_choice_name = "RocK"
        print("Computer choice is Rock")
    elif comp_choice == 2:
        comp_choice_name = "Paper"
        print("Computer choice is Paper")
    else:
        comp_choice_name = "Scissors"
        print("Computer choice is Scissor")
    
    print(user_choice_name, 'Vs', comp_choice_name)
    
    #Checks for draw
    if user_choice == comp_choice:
        print('Its a Tie', end="")
        result = "TIE"

    # condition for winning
    if (user_choice == 1 and comp_choice == 2):
        print('Paper Wins', end="")
        result = 'Paper'
        comp_score = comp_score + 1
        
    elif (user_choice == 2 and comp_choice == 1):
        print('Paper Wins', end="")
        result = 'Paper'
        user_score = user_score + 1
        
    elif (user_choice == 1 and comp_choice == 3):
        print('Rock Wins', end="")
        result = 'Rock'
        user_score = user_score + 1
    elif (user_choice == 3 and comp_choice == 1):
        print('Rock Wins', end="")
        result = 'RocK'
        comp_score = comp_score + 1
    elif (user_choice == 2 and comp_choice == 3):
        print('Scissors Wins', end="")
        result = 'Scissors'
        comp_score = comp_score + 1
    elif (user_choice == 3 and comp_choice == 2):
        print('Scissors Wins', end="")
        result = 'Scissors'
        user_score = user_score + 1

    #Printing either user or computer wins or draw
    if result == 'TIE':
        print("\n <== Its a draw ==>")
    elif result == user_choice_name:
        print("\n <== User wins ==>")
    else:
        print("\n <== Computer wins ==>")

    print("User Score :",user_score)    
    print("Computer Score:",comp_score)

    print("Do you want to play again? (Y/N):")

    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing")

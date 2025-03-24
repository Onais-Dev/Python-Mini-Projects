import random

rps = ['0', '1','2']
# Ask a user about what they want choose 0 for Rock. 1 for paper, 2 for scissors

user_choice = int(input("Choose one of these: 0 for Rock, 1 for Paper, 2 for scissors:"))

if user_choice == 0:
    print("Rock")
    
elif user_choice == 1:
    print("paper")
    
elif user_choice == 2:
    print("Scissors")




# Computer will randomly choose between 3 of them with random module

comp_choice = int(random.choice(rps))


if comp_choice == 0:
    print("Rock")
    
elif comp_choice == 1:
    print("Paper")
    
elif comp_choice == 2:
    print("Scissors")
    
# Rules
# compare the choices of user and computer and determine who lost or win or draw

if comp_choice == user_choice:
    print("draw")

elif comp_choice == 0 and user_choice == 1 or comp_choice == 2 and user_choice == 1 or comp_choice == 0 and user_choice == 2:
    print("You loss")

elif comp_choice == 1 and user_choice == 0 or comp_choice == 1 and user_choice == 2 or comp_choice == 2 and user_choice == 0:
    print("You Won")













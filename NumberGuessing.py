#Computer will randomly choose a number
# User can input the number to guess the number
# In 10 attempts"""Track the number of attempts"""
#Provide Hints to the inputs either the guess is high or lower 

import random
random_number = random.randint(1, 100)
# print(random_number)
attempts = 1
user_input = int(input("Guess The Number Range (1 - 100): "))

while user_input != random_number and attempts<=10:
    print("Attempt:", attempts)
    user_input = int(input("Guess The Number Range (1 - 100): "))
    attempts +=1
    if attempts >= 10:
          print("Correct Number",random_number)
          print("Game Over")
    

if user_input==random_number:
        print("You got it right on", attempts, "Attempts")
    


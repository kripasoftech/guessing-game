# This program is designed to play guessing game. User will have three attempt to correct number between 1 and 10
 
# Importing random module to get random number between range
import random

# Taking input from user to guess number as integer to match with random number
guess_number = int(input("Please enter a number between 1 and 10 to correct your guess: "))

# Defining correct number using int module function
correct_number = random.randint(1, 10)

# Initiating a valiable to count attempts
attempt = 3

# Using while loop to run statement multiple times
# Matching input with correct_number using control function (if)
while attempt > 0:
    if guess_number == correct_number:
        print(f"Congratulations! You have got the right number, it is {correct_number}.")

        # Stopping the loop after matching guess_number with correct_number
        break
    else:

        # Reducing attempt count after failing the one 
        attempt -= 1

        # Retaking the user input for remaining attempt
        if attempt > 0:
            guess_number = int(input("Wrong, please try again: "))
        else:
            # Ending the program after 3 attempts
            print(f"Sorry! Game is over, the correct number is {correct_number}")

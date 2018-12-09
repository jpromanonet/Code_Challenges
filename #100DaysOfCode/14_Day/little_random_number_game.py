# This is a guess the number game

# Call imported functions

import random

# Define global scope

guess = None
secret_Number = random.randint(1, 100)
print('I am thinking in a number between 1 and 100')

# Ask for user input

for guess_Taken in range (1, 6):
    print('Take a guess')
    guess_Taken = int(input())

    if guess_Taken < secret_Number:
        print('You are way below the number')
    elif guess_Taken > secret_Number:
        print('You are betting too high, kiddo')
    else:
        break # This one is the correct guess!

if guess == secret_Number:
    print('You are fucking awesome! you guessed my number in ' +str(guess_Taken) + ' tries!')
else:
    print('Nope, the number i was thinking of was ' +str(secret_Number))

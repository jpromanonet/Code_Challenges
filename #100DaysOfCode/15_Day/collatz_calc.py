# creating functions

def collatz(number): # Function to create the collatz secuence
    # If number is even
    if number % 2 == 0:
        return number // 2
    # if number is odd
    elif number % 2 == 1:
        return 3 * number + 1

# Creating the program logic

# Input data

print('Please, state a number')
start_Number = input()

# Processing data input

final_Number = collatz(int(start_Number))
print(final_Number)

# Conditional process

while final_Number != 1:
  final_Number = collatz(int(final_Number))
  print(final_Number)
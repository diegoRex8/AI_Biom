#Generates a random number between 1 and 100, and then asks the user to guess the number

from random import randint

# Generate a random number between 1 and 100
target_number = randint(1, 100)

# Initialize a variable to keep track of the number of guesses
attempts = 0

print('Number Guessing Game')
print('Try to guess the number between 1 and 100.')
print('------------------------------------------')

while True:
    try:
        # Get the user's guess
        user_guess = int(input('Enter your guess: '))
        attempts += 1

        if user_guess < target_number:
            print('Too low! Try again, higher.\n')
        elif user_guess > target_number:
            print('Too high! Try again, lower.\n')
        else:
            print('Congratulations! You guessed the number',target_number,'in',attempts,'attempts.')
            break  # Exit the loop when the user guesses correctly
    except ValueError:
        print('Error. Please enter a valid number.')

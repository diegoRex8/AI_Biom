import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "orange", "pear", "melon", "grape", "mango"]

# Select a random word from the list
target_word = random.choice(word_list)

# Initialize variables
guessed_word = ['_' for _ in target_word]
max_attempts = 6
attempts = 0
guessed_letters = []

print("Welcome to Hangman (Fruits' Version)")

while attempts < max_attempts:
    print(' '.join(guessed_word))
    guess = input('Guess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Invalid input. Please enter a single letter.')
        continue

    if guess in guessed_letters:
        print('You already tried that letter. Try another one.')
        continue

    guessed_letters.append(guess)

    if target_word.find(guess) != -1:
        positions = [i for i, letter in enumerate(target_word) if letter == guess]
        for position in positions:
            guessed_word[position] = guess
    else:
        attempts += 1
        print('Wrong guess! You have',(max_attempts - attempts),'attempts left.')

    if "".join(guessed_word) == target_word:
        print('Congratulations! You guessed the word:',target_word)
        break

if attempts >= max_attempts:
    print("Sorry, you're out of attempts. The word was:", target_word)

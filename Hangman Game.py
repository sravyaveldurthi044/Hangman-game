import random

# List of words
words = ["apple", "tiger", "house", "chair", "water"]

# Randomly choose a word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Number of attempts
attempts = 6

print("Welcome to Hangman Game!")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check letter
    if guess in word:
        print("Correct Guess!")

        # Replace blanks with guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        attempts -= 1

# Final Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)

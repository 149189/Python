#Create the classic Hangman game where the user guesses letters to form a word.

import random

def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "algorithm"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Current word: ", " ".join(display_word))

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            guessed_letters.add(guess)
            incorrect_guesses += 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()

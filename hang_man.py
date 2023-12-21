import random  # Import the random module for random word selection
from words import words  # Import the list of words from the words module
import string  # Import the string module for accessing string constants


def get_valid_word(words):
    # Choose a valid word from the list of words
    word = random.choice(words)
    while " " in word or "-" in word:
        # Keep choosing until a word without spaces or dashes is found
        word = random.choice(words)
    return word.upper()  # Convert the word to uppercase


def hang_man():
    word = get_valid_word(words)  # Get a valid word to guess
    word_letters = set(word)  # Convert the word to a set of unique letters
    alphabet = set(string.ascii_uppercase)  # Create a set of all uppercase letters
    used_letters = set()  # Initialize an empty set to store used letters
    lives = 6  # Initialize the number of lives

    while len(word_letters) > 0 and lives > 0:
        print(
            "You have",
            lives,
            "lives left and you have used these letters: ",
            " ".join(used_letters),
        )

        word_list = [
            letter if letter in used_letters else "-" for letter in word
        ]  # Create a list with the guessed letters and dashes for unguessed letters

        print(
            "Current word: ", " ".join(word_list)
        )  # Print the current state of the word

        user_letter = input(
            "Guess a letter: "
        ).upper()  # Get user's letter and convert it to uppercase
        if user_letter in alphabet - used_letters:
            # Check if the letter is in the remaining alphabet set (not used yet)
            used_letters.add(user_letter)  # Add the letter to the used_letters set
            if user_letter in word_letters:
                word_letters.remove(
                    user_letter
                )  # Remove the letter from the word_letters set
            else:
                lives -= (
                    1  # Decrement the number of lives if the letter is not in the word
                )
        elif user_letter in used_letters:
            print(
                "This letter is already used. Try again!"
            )  # Prompt if the letter is already used
        else:
            print(
                "Invalid character. Please try again."
            )  # Prompt if the input is not a valid letter

    if lives == 0:
        print(f"Sorry, you lost! The word was {word}")  # Print the losing message
    else:
        print(
            f"Congratulations, you guessed the word {word} correctly!!"
        )  # Print the winning message


hang_man()  # Call the hang_man function to start the game

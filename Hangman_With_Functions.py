import random

def random_word(): # Function for a list of words used for the hangman
    words =[
        "ephemeral",
        "serendipity",
        "mellifluous",
        "ineffable",
        "petrichor",
        "sonder",
        "limerence",
        "quixotic",
        "susurrus",
        "defenestration",
        "sonder",
        "elixir",
        "halcyon",
        "sonorous",
        "ethereal"
    ]
    return random.choice(words)

def print_gallows(number_of_body_parts): # Function for list of graphics for hangman (used from a personal project of mine)
    graphic = [
        """
            +-------+
            |       |
            |       
            | 
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / |
            |
         ==============
        """]
    print(graphic[number_of_body_parts])

def ask_user_for_guess(hidden_word, letters_guessed):
    while True:
        letter_guessed = input("\nGuess the letter: ").strip().lower()

        if len(letter_guessed) != 1: # Asks user to try again
            print("Please enter only a single letter.")
            continue

        if letter_guessed in letters_guessed: # Asks user to try again
            print("You already guessed that letter.")
            continue

        letters_guessed.append(letter_guessed)

        if letter_guessed in hidden_word:  # Correct guess
            return letter_guessed, True
        else: # Wrong guess. Returns False to mark as wrong guess
            return letter_guessed, False

def print_hidden_word(hidden_word, letters_guessed):
    for letter in hidden_word: # for each character in the word
        if letter in letters_guessed:
            print(letter, end=" ")  # Print the correct letter
        else:
            print("_", end=" ")  # Print an underscore for missing letters

def is_game_over(hidden_word, letters_guessed, number_of_incorrect_guesses):
    if all(letter in letters_guessed for letter in hidden_word): # Check if the player has guessed all letters
        print(f"\nCongratulations! You guessed the word: {hidden_word}!")
        return True  # Game over

    elif number_of_incorrect_guesses == 6: # Check if the player has reached max incorrect guesses
        print(f"\nGame Over! The correct word was: {hidden_word}")
        return True  # Game over

    return False  # Current game continues

def main():
    while True: # Loop to replay the game
        word = random_word() # Calls random word
        letter_list = [] # List for letters guessed
        wrong_guesses = 0 # Wrong guess variable

        print('\n--- Hangman ---')
        print_gallows(wrong_guesses) # Shows the initial graphic of the gallows
        while wrong_guesses < 6:  # Stop when max wrong guesses reached
            print_hidden_word(word, letter_list) # Calls function to display "_" or correctly guessed letters
            letter_guessed, letter_condition = ask_user_for_guess(word, letter_list) # Calls function for user to guess
            print('\n')
            if not letter_condition:  # If the guess is incorrect
                wrong_guesses += 1  # Increment wrong guesses
                print_gallows(wrong_guesses)  # Immediately update the gallows

            # Check if player won or lost by calling function to check each iteration of game loop for wrong guesses or word is found
            if is_game_over(word, letter_list, wrong_guesses) == True:
                break  # Exit loop if game is over

        # Ask user if they want to play again
        play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()
        if play_again != 'y' or play_again != 'yes': # If user inputs anything but Yes or y, loop is broken ending the game
            print("\nThanks for playing!")
            break  # Exit the game loop

main() # Runs program
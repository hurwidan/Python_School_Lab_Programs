import random
def string():
    user_string = input("Enter a word: ").strip().replace(" ", "")
    array_numbers = [0] # Starts with first index
    string_length = (len(user_string) - 1) # Finds string length based on sequence of characters

    for i in range(string_length): # Creates sequence of characters to implement into array
        array_numbers.append(i + 1)

    new_string = '' #Empty variable for the scrambled string

    while len(new_string) != (string_length+1): # While the new string character length is not equal to the inputted string, the while loop will repeat
        random_choice = random.choice(array_numbers) # Chooses a random integer from the array
        new_string += user_string[random_choice] # Adds the character that corresponds to the integer into the new string
        if random_choice in array_numbers: # If statement to remove already chosen integer from array
            array_numbers.remove(random_choice)

    new_string_length = (len(new_string) -1) #Finds new string's character total based on sequence of characters

    print(f"\nScrambled Word: {new_string}")

    print(f"\nOriginal Word's Total Characters: {string_length}") # To compare for accuracy
    print(f"Scrambled Word's Total Characters: {new_string_length}") # To compare for accuracy

string()

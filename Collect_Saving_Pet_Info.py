def info_collection(): # Function to gather pet info
    name = input("Enter Pet's name: ")
    species_type = input("Enter Pet's Species: ")
    breed = input("Enter Pet's Breed: ")
    color = input("Enter Pet's Color: ")
    size = input("Enter Pet's Size: ")
    weight = input("Enter Pet's Weight: ")
    return name, species_type, breed, color, size, weight

def info_saving(name, species_type, breed, color, size, weight): # Function to save pet info into text file
    file = open(f'information.txt', 'a') # If file doesn't exist then creates file
    file.write(f'Name: {name}\n')   # If the file exists, appends new info below existing info
    file.write(f'Species: {species_type}\n')
    file.write(f'Breed: {breed}\n')
    file.write(f'Color: {color}\n')
    file.write(f'Size: {size}\n')
    file.write(f'Weight: {weight}\n')
    file.write('\n')
    file.close() # Closes file

def main():
    while True: # While True loop to allow user to put as much pet info as they want
        name, species_type, breed, color, size, weight = info_collection() # Calls collection function
        info_saving(name, species_type, breed, color, size, weight) # Calls saving function
        user_choice = input("Would you like to submit more data? (y/n): ") # Allows user to put more info of other pets in
        if user_choice == 'y' or user_choice == 'Y':
            continue
        elif user_choice == 'n' or user_choice == 'N':
            break
        else:
            print("Please enter 'y' or 'n'")

main()
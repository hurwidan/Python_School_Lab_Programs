import random
import dnd_character_creation


def get_race(): # Function for selecting race
    """Function for selecting a race from dnd_races."""
    races = dnd_character_creation.dnd_races

    # Creating a numbered list of races
    counted_races = {str(index): (race, description) for index, (race, description) in enumerate(races.items(), start=1)}

    # Displaying available races
    for index, (race, description) in counted_races.items():
        print(f'{index}. {race} ~ {description}')

    # User input with validation
    while True:
        user_input = input("\nInput the number of the desired race: ").strip()
        if user_input in counted_races:
            selected_race, selected_description = counted_races[user_input]
            print(f'\n{selected_race} - {selected_description}')
            return selected_race, selected_description
        else:
            print("Invalid selection. Please enter a valid number from the list.")

def get_name(): # Function to give the user a name for their character
    name = input("What is your character's name?: ")
    return name

def sum_of_four_sided_dice_with_lowest_dropped(): # Function to give the user their available points to use for stats
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)

    rolls = [
        num1,
        num2,
        num3,
        num4
    ]

    smallest_roll = min(rolls) # Finds smallest roll
    rolls.remove(smallest_roll) # Removes that roll from the list
    total_points = sum(rolls) # Gets sum of all rolls combines

    return total_points # Returns total available points for user to use to customize stats

def assign_points_to_stats(name, race): # Function for user to apply points to their stats
    stats = dnd_character_creation.dnd_race_stats[race]
    print(f"\n--- {name}'s Default Stats ---\n")
    for stat, points in stats.items():
        print(f"    {stat}: {points}")

    total_points = sum_of_four_sided_dice_with_lowest_dropped() # Total allowed points retrieved from function

    print(f'\nTotal Points: {total_points}')

    while total_points > 0: # While loop that doesn't stop till all available points are used
        for stat in stats.keys():
            if total_points == 0:
                break
            print(f"\nPoints remaining: {total_points}")
            try:
                while stat:
                    user_input = input(f"How many points would you like to add to {stat}? (Type 'f' to Skip) ").strip()
                    if user_input.lower() == "f" or user_input == "": #  Skips the stat
                        break
                    stat_points = int(user_input)
                    if stat_points > total_points: # Repeats the user input for the stat if input is too high
                        print("Not enough points! Please try again.")
                    elif stat_points < 0: # Repeats the user input for the stat if input is negative
                        print("You cannot assign negative points. Please try again.")
                    else:
                        stats[stat] += stat_points # Adds points to stat
                        total_points -= stat_points # Removes points from available points
                        break
            except ValueError:
                print("Invalid input.")

    print("\nFinal Stats:")
    for stat, points in stats.items():
        print(f"    {stat}: {points}")
    return stats # Returns custom stats

def get_ability_modifier(name, race): # Function for giving the stat modifiers
    stats = assign_points_to_stats(name, race)
    print("\n--- Advantages ---\n")
    modifiers = {}
    for stat, points in stats.items():
        print(f"    {stat}")
        modifier_roll = random.randint(1, 20) # Rolls a D20
        if modifier_roll == 20: # Rolls a D10 if 20 is rolled from D20
            modifier_roll += random.randint(1, 10)

        modifier = (modifier_roll - 10) // 2 # Calculation for the modifier

        if modifier >= 0:
            modifier = f'+{modifier}' # Adds a + if its 0 or greater

        modifiers[stat] = modifier

        print(f'      Rolled: {modifier_roll}')
        print(f'      Modifier: {modifier}')

    print("\n--- Final Stats w/ Advantages ---\n")
    final_stats = {}
    for stat, points in stats.items(): # For loop to store the stats, points, and their modifiers into a final stat list
        final_stats[stat] = {
            "Stat": stat,
            "Points": points,
            "Modifier": modifiers[stat]
        }
    for stat, info in final_stats.items():
        print(f"    {info['Stat']}: {info['Points']} ({info['Modifier']})")
    return final_stats

def menu(): # Function for displaying the actions and giving the user up to 4 actions
    actions = {
        '1': 'Attack',
        '2': 'Negotiate',
        '3': 'Search',
        '4': 'Eat',
        '5': 'Exit'
    }
    race, description = get_race()
    name = get_name()
    print(f"\nName: {name}")
    print(f"Race: {race}")

    final_stats = get_ability_modifier(name, race)
    actions_taken = 0 # Count for actions taken
    max_actions = 4 # Max actions allowed

    while actions_taken < max_actions: # Loop allowing user to go up to the max count of actions
        print(f"\n--- Actions ({actions_taken}/{max_actions}) ---\n")
        for num, action in actions.items():
            print(f"{num}. {action}")

        choice = input('\nSelect an action (1-5): ').strip()

        if choice in actions: # If else allowing user to not use all actions
            if actions[choice] == 'Exit':
                print("\nYou decide to stop taking actions.")
                break

            perform_action(actions[choice], final_stats)
            actions_taken += 1 # Once an action is made, its sent to the action count

            if actions_taken == max_actions:
                print("\nYou've ran out of actions!")
                break
        else:
            print("Invalid. Please choose a valid number.")

def perform_action(action, stats): # Function for Selecting Actions
    if action == 'Attack':
        return attack(stats)
    elif action == 'Negotiate':
        return negotiate(stats)
    elif action == 'Search':
        return search(stats)
    elif action == 'Eat':
        return eat(stats)

def get_stat_choice(stats, options): # Function that gives the user an option for actions that are given choices for stats
    while True:
        if len(options) == 1: # If there is only one option then it carries forward without user input
            user_input = options[0]
        else:
            user_input = input(f"Use {options[0]} or {options[1]}?: ").strip().title() # Choice between stats for an action
        if user_input in stats:
            return user_input, stats[user_input]['Modifier'] # Returns the chosen stat and its modifier
        else:
            print("Invalid. Choose a valid ability.")

def attack(stats): # Function for attack action
    roll = random.randint(1, 20)
    stat_choice, stat_modifier = get_stat_choice(stats, ['Strength', 'Dexterity']) # Goes through stat_choice function

    attack_score = roll + int(stat_modifier) # Gets attack score based on role and stat modifier
    print(f"\nAttack Roll: {attack_score}")

    if attack_score >= 12: # If roll is equal or greater than 12, the attack will be successful
        print(f'\nSuccessful Hit!')
        damage_roll = random.randint(1, 6)
        damage = damage_roll + int(stat_modifier) # Gets damage score based on roll and stat modifier
        if damage <= 0: # If statement that doesnt allow negative damage
            damage = 0
        print(f'Damage Dealt: {damage}')
        return damage
    else:
        print('\nMissed!')
        return 0

def negotiate(stats): # Function for the negotiation action

    roll = random.randint(1, 20)
    stat_choice, stat_modifier = get_stat_choice(stats, ['Charisma']) # Goes through stat_choice function

    score = roll + int(stat_modifier)  # Gets negotiate score based on role and stat modifier
    print(f"\nNegotiation Roll: {score}")

    if score >= 15: # If roll is equal or greater than 15, negotiation will be a success
        print("You've successfully negotiated a Truce!")
    else:
        print("Negotiation Failed!")

def random_treasure(): # Function that returns common treasure or legendary treasure based on chance
    roll = random.randint(1, 20)
    common_treasure = ["Gems", "Gold", "Jade Figurine", "Common Gear"]
    legendary_treasure = [
        "Sword of Kas", "Eye of Vecna", "Hand of Vecna", "Ring of Three Wishes",
        "Ring of Invisibility", "Horn of Valhalla", "Rod of Lordly Might",
        "Wand of Orcus", "Luck Blade"
    ]

    if roll >= 15: # If roll is equal or greater than 15, legendary treasure will be returned
        return random.choice(legendary_treasure)
    else: # Common treasure is returned if below 15
        return random.choice(common_treasure)

def search(stats): # Function for the search action
    roll = random.randint(1, 20)
    stat_choice, stat_modifier = get_stat_choice(stats, ['Intelligence', 'Wisdom']) # Goes through stat_choice function

    search_score = roll + int(stat_modifier) # Gets search score based on role and stat modifier
    print(f"\nSearch Roll: {search_score}")

    if search_score >= 12: # If search_score is greater than or equal to 12 then the user finds treasure
        treasure = random_treasure()
        print(f"\nFound Treasure: {treasure}!")
    else: # If search_score is less than 12 then the user doesn't find anything
        print("\nYou found...... nothing.")

def eat(stats): # Function for the eat action. The food is always rancid
    print("Your food is rancid! Let's hope you have a strong stomach!\n")
    roll = random.randint(1, 20)
    stat_choice, stat_modifier = get_stat_choice(stats, ['Constitution']) # Goes through stat_choice function

    score = roll + int(stat_modifier)  # Gets search score based on role and stat modifier
    print(f"\nEating Roll: {score}")

    if score >= 10: # If score is greater than or equal to 10 then the user eats the food without a problem
        print("You were able to handle the food!")
    else:
        print("You were not able to handle the food! You feel sick and need to rest.")

menu()
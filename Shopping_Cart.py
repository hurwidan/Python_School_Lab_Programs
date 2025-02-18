print("Welcome to Daniel's Shopping Cart Calculator")
print('\n--- Shopping Cart ----')
def cart(): # Function for user input of cart items and their cost and to return list of cart items with cost
    cart = {} # Cart variable list
    while True:
        try:
            cart_item_name = input("\nEnter the name of the item (or type 'f' to finish): ").strip()# Input name of item
            if cart_item_name.lower() == 'f': # Skips to finish function
                print('\n--- Receipt ---\n')
                break
            while True:
                try:
                    cart_item_cost = input(f"Enter the cost for '{cart_item_name}':").strip() # Input cost of item
                    if cart_item_cost == str: # Throws error if string
                        raise ValueError
                    elif float(cart_item_cost) <= 0: # Throws error if negative
                        raise ValueError
                    else: # Adds Item with cost and formats cost correctly to #.##
                        cart_item_cost = float(cart_item_cost)
                        cart[cart_item_name] = format(cart_item_cost, '.2f')
                        break
                except ValueError: # Error text for when error is raised
                    print("\nInvalid input. Please enter a valid number for the cost.")

        except ValueError:
            print("Invalid input.")

    return list(cart.items())

def discounts(total): # Function for user input of discounts and returning counts of discounts used
    codes = { # List of hardcoded discount codes
        'JUMPSTR33T',
        'T3D',
        'FAM1LYGUY',
        'AD3NTUR3',
        'T1M3',
        'T2M3',
        'T3M3',
        'T4M4',
        'SP33DB0AT',
        'SKYFALL99',
        'QU1CKRUN',
        'TR4V3L1NG',
        'W1NDBREAK',
        'H1DDENKEY',
        'BL1ZZ4RD',
        'ST33LR0AD',
        'SH4D0WF1GHT',
        'R34LITY42',
        'L0STW0RLD',
        'P1R4TES77',
        'C0D3BR34K',
        'MYST1CALX',
        'THUND3RD0M3',
        'FUTUR35T3P',
        'V1RTUALRUN',
        'CYB3RC0D3',
        'SKYW4LK3R',
        'DR4G0NT41L',
        'P0W3RUP99',
        'QUANTUMX'
    }
    total_count = 0
    code_count = 0
    if total >= 100:
        total_count = 1

    question = input("Do you have a discount (Y/N)?:") # Input of whether user has discount
    while True:
        if question.lower() == 'yes' or question.lower() == 'y': # Initiates while loop for inputting existing codes
            while codes:
                code = input("\nInput Discount Code (or type 'f' to finish): ").strip() # Input Discount Code
                if code in codes: # Removes used discount from list
                    total_count += 1
                    code_count += 1
                    codes.remove(code)
                    print(f"Discount applied successfully!")
                elif code.lower() == 'f': # Finishes function
                    print('\n')
                    break
                elif total >= 100 & code_count >= 18 or code_count >= 20: # Condition for limit of Discounts applied
                    print('\nNo more Discounts can be applied!')
                else: # Error for invalid discount code
                    raise ValueError("\nInvalid. Please enter a valid code for the discount.")

                if not codes:
                    print("\nAll discount codes have been applied.")

        elif question.lower() == 'no' or  question.lower() == 'n': # Returns current discount counts as is
            return code_count, total_count
        else:
            raise ValueError("\nInvalid input.")

        return code_count, total_count


def discount_cal(discount_count, total): # Discount Calculator function returning Discount Total Off and Grand Total
    discount_percentage = float(discount_count * .05) # Calculates inputted discounts

    if total >= 100: # Calculates total with discounts including discount for over $100
        cart_discount = float((total * .1) + (total * discount_percentage))
    else: # Calculates total with discounts
        cart_discount = float(total * discount_percentage)


    grand_total = round(float(total - cart_discount), 2)

    return cart_discount, grand_total


total = 0

for item, item_cost in cart(): # Initialization of Cart Function and total of combined item costs
    total += float(item_cost)
    print(f'{item}: ${item_cost}')

total = round(total, 2)

count, total_discount = discounts(total) # Initialization of discount function

print(f'\nTotal: ${format(total, '.2f')}')
print(f'\nDiscounts Used: {total_discount}')

cart_discount, grand_total = discount_cal(count, total) # Initialization of discount calculator function

print(f'\nDiscount Off: ${format(cart_discount, '.2f')}')
print(f'Grand Total: ${format(grand_total, '.2f')}')

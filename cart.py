def add_item(cart, item, price, quantity): # Function to add items or edit the quantity of an existing item
    if item not in cart:
        price = format(price, '.2f')
        cart[item] = {"item": item, "price": price, "quantity": quantity}
    else:
        cart[item]["quantity"] = quantity

def remove_item(cart, item): # Function to remove items
    if item in cart:
        del cart[item]
    else:
        print("Item not in cart.")
def calculate_total(cart): # Function to calculate and return the current total
    total = 0
    for item in cart:
        total += float(cart[item]["price"]) * float(cart[item]["quantity"])

    total = round(total, 2)
    return total

def display_cart(cart): # Function to display the current cart and total
    total = format(calculate_total(cart), '.2f')
    print("\n--- Cart ---\n")
    for item in cart:
        print(f'{cart[item]["quantity"]}   {cart[item]["item"]} ~ ${cart[item]["price"]}')
    print(f"    Total: ${total}")

def main():
    cart = {}
    print("\n--- Shopping Cart Simulator ---\n")
    while True:
        # Adding the first item to the cart
        while True:
            item_name = input("Add item to cart: ")
            item_cost = input("How much does it cost?: ")
            item_quantity = input("What's the quantity?: ")

            try:
                item_cost = float(item_cost)
                item_quantity = int(item_quantity)
                add_item(cart, item_name, item_cost, item_quantity)
                break
            except ValueError:
                print("Invalid inputs.")

        # Menu loop for user choices
        while True:
            print("\n")
            user_choice = input(
                "Would you like to: \n"
                "  1) Add/Edit Item\n"
                "  2) Remove Item\n"
                "  3) View Cart\n"
                "  4) Checkout\n"
                "Enter your choice: "
            ).strip().lower()

            if user_choice in ["1", "add", "edit"]: # Allows choice by number or specific key words relating to action
                item_name = input("Input item: ")

                if any(item_name in item for item in cart):  # Checks if the item is in the cart
                    item_quantity = input("What's the quantity?: ")
                    try:
                        item_quantity = int(item_quantity)
                        add_item(cart, item_name, 0, item_quantity)
                    except ValueError:
                        print("Invalid input.")
                else:
                    item_cost = input("How much does it cost?: ")
                    item_quantity = input("What's the quantity?: ")
                    try:
                        item_cost = float(item_cost)
                        item_quantity = int(item_quantity)
                        add_item(cart, item_name, item_cost, item_quantity)
                    except ValueError:
                        print("Invalid inputs.")

            elif user_choice in ["2", "remove"]: # Allows choice by number or specific key words relating to action
                print("\n")
                item_name = input("Input item to remove: ")
                remove_item(cart, item_name)

            elif user_choice in ["3", "view"]: # Allows choice by number or specific key words relating to action
                print("\n")
                display_cart(cart)

            elif user_choice in ["4", "checkout"]: # Allows choice by number or specific key words relating to action
                display_cart(cart)
                break  # Exits menu and ends loop. Consequently ending the program.

            else:
                print("Invalid option.")
        break

main()
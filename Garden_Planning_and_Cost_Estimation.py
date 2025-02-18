print('Welcome to Garden Planning and Cost Estimations!')

# Function for inputting the Garden dimensions & raising errors if value is less than or equal to 0
def dimension_input(user_input):
    try:
        value = float(input(user_input))
        if value <= 0:
            raise ValueError('Dimensions must be greater than zero!')
        return value
    except ValueError:
        print('Try again! Input must be greater than zero!')

# Function for inputting the requested area & raising errors if value is more than the available area or less than 0
def area_input(prompt, available_area):
    while True:
        try:
            area = float(input(prompt))
            if area < 0 or area > available_area:
                raise ValueError("Requested area must be between zero and the available area!")
            return area
        except ValueError:
            print("Enter a different value.")

print('\n--- Garden Dimension Calculation ---\n')

# Using the dimension input function to collect the length and width of the Garden
length = dimension_input('Input Garden length: ')
width = dimension_input('Input Garden width: ')

# Garden Area calculation
dimensions = round((length * width), 2)

print(f'\nGarden Dimensions: {dimensions} squared ft')

# List of Available Plants
print("\n--- Available Plants ---\n")

plants = {
    "Roses": 2.50,
    "Tulips": 1.75,
    "Daisies": 1.00,
    "Bonsai Trees": 45.00,
    "Focal Wild Flowers": 1.50,
    "Evergreen Shrubs": 5.00,
    "Calla Lilies": 10.00,
    "Snowdrops": 4.00,
    "Grape Hyacinths": 9.00,
    "Crocuses": 6.50,
    "Allium": 4.75,
    "Cannas": 5.00,
    "Hyacinths": 9.00,
    "Iris": 11.00
}

# Displaying each plant with its cost per square foot
for plant, cost in plants.items():
    formatted_cost = format(cost, '.2f')
    print(f'{plant}: ${formatted_cost} per square foot')

print('\n--- Garden Planning ---\n')

# Variables to store requested area and allocated areas for plants
requested_area = 0
plant_area = {}

# Loop to collect area input for each plant and calculate remaining garden area
for plant in plants.keys():
    available_area = round(dimensions - requested_area, 2)

    # Stop the loop if no available area is left
    if available_area == 0:
        print('There is no more available area! Continuing to the Cost Estimation Process...')
        break
    else:
        print(f'Available area: {available_area} square ft')

    # Using area_input function
    area = area_input(f"\nEnter area to allocate for {plant}: ", available_area)

    # Skip the plant if area input is 0
    if area == 0:
        continue

    # Update requested area and store the allocated area for the plant
    requested_area += area
    plant_area[plant] = plant_area.get(plant, 0) + area

print("\n--- Requested Plants ---\n")

# Displaying the requested area for each plant
requested_area = 0
for plant, area in plant_area.items():
    requested_area += area
    print(f'{plant}: {area} square ft')

# Calculate and display remaining garden space
available_area = round(dimensions - requested_area, 2)

print(f'\nTotal Requested Area for Plants: {requested_area} square ft')
print(f'Leftover Space: {available_area} square ft')

print("\n--- Cost Estimation ---\n")

# Variables to store for calculated costs and combined total
total_costs = {}
total = 0

# Calculate and display cost for each plant and total cost
for plant, area in plant_area.items():
    if plant in plants:
        total_costs[plant] = plants[plant] * area
    else:
        total_costs[plant] = 0

for plant, cost in total_costs.items():
    cost = round(cost, 2)
    print(f'{plant}: ${format(cost, ".2f")}')
    total += cost

# Michigan Sales Tax (for funsies)
sales_tax = 0.06

# Tax and Grand Total Calculations
estimated_tax = round(total * sales_tax, 2)
grand_total = round(total + estimated_tax, 2)

print(f'\nTotal: ${format(total, ".2f")}')
print(f'Tax: ${format(estimated_tax, ".2f")}')
print(f'\nGrand Total: ${format(grand_total, ".2f")}')
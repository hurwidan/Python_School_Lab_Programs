import math
import random

# Function for Affirmation Generator
def affirmation_generator():
    affirmations = [
        "I am worthy of love and respect.",
        "I am constantly growing and evolving into my best self.",
        "Challenges are opportunities for growth, and I embrace them.",
        "I am grateful for my healthy body and mind.",
        "I am capable of achieving great things."
    ]
    # Selects and prints a random affirmation from list of five affirmations
    affirmation = random.randint(1, 5)
    return print(f'{affirmations[affirmation-1]}')

# Function for Quadratic Equation Intercept Finder
def quadratic_equation_intercept_finder(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        # No real roots, return an "No intercepts exist."
        return print("No intercepts exist.")
    elif discriminant == 0:
        # One real root (double root), return a single x-intercept
        x = -b / (2 * a)
        return print((x, ))
    else:
        # Two distinct real roots, return two x-intercept
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)

        return print((x1, x2))

print(f'\n--- Affirmation Generator ---\n')

affirmation_generator()

print(f'\n--- Quadratic Equation Intercept Finder ---\n')

# User input for Quadratic equation variables
a = int(input(f'Input a: '))
b = int(input(f'Input b: '))
c = int(input(f'Input c: '))

quadratic_equation_intercept_finder(a, b, c)
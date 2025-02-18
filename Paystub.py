# Input for Name, Hourly Wage, & Total hours for the week
name = input("Enter your name: ")
wage = float(input("Enter your hourly wage: "))
hours = float(input("Enter your hours for the week: "))

# Calculations of Salary Before Taxes, Estimated Taxes, and Net Salary
weekly_sal = wage * hours
tax_rate = .1
estimated_tax = weekly_sal * tax_rate
net_salary = weekly_sal - estimated_tax

# Pay Stub Display
print("\n--- Weekly Salary Summary ---")
print(f'Name: {name}')
print(f'Weekly Salary Before Taxes: ${format(weekly_sal, '.2f')}')
print(f'Estimated Taxes (10%): ${format(estimated_tax, '.2f')}')
print(f'Net Salary: ${format(net_salary, '.2f')}')
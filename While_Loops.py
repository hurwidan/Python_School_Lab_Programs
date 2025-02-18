def user_today(): # Function to gather the date of today from user
    print("--- Today's Date ---")
    user_month = int(input("Enter the month: "))
    user_day = int(input("Enter the day of the month: "))
    user_year = int(input("Enter the year: "))

    return user_day, user_month, user_year

def user_date(): # Function to gather date of the future from user
    print("\n--- Future Date ---")
    user_month = int(input("Enter the month (1-12): "))
    user_day = int(input("Enter the day (1-31): "))
    user_year = int(input("Enter the year (2025-2099): "))

    return user_month, user_day, user_year

def date_calculation(user_month, user_day, user_year, future_month, future_day, future_year):

    future_year = future_year * 365 # Converts years to days of future date
    future_month = future_month * 31 # Converts months to days of future date
    future_days = future_year + future_month + future_day # Combines all days of future date

    user_year = user_year * 365 # Converts years to days of current date
    user_month = user_month * 31 # Converts months to days of current date
    user_days = user_year + user_month + user_day # Combines days

    days_till = future_days - user_days # Subtracts current total days from future total days to get days till


    return days_till

def main():
    user_day, user_month, user_year = user_today() # Calls current date function
    future_month, future_day, future_year = user_date() # Calls future date function

    days_till = date_calculation(user_month, user_day, user_year, future_month, future_day, future_year) #Calls calculation function

    print(f'Days until {user_month}/{user_day}/{user_year}: {days_till} days') # Displays days till future date

main()
class ElectricVehicle:
    def __init__(self): # Initialize vehicle attributes with default values
        self.max_kilowatt_hours = 75.0  # Maximum battery capacity (kWh)
        self.current_kilowatt_hours = 50.0  # Current battery charge (kWh)
        self.color = "White"  # Vehicle color
        self.make = "Tesla"  # Vehicle manufacturer
        self.model = "Model 3"  # Vehicle model
        self.kilometers_per_kilowatt_hour = 5.0  # Efficiency in km per kWh

    def get_vehicle_info(self):  # Return formatted vehicle details
        return (f"{self.color} {self.make} {self.model}\n- {self.kilometers_per_kilowatt_hour} km/kWh\n- "
                f"{self.max_kilowatt_hours} Max kWh Battery\n- {self.current_kilowatt_hours} Current kWh Battery")

    def set_color(self): # Prompt user to update the vehicle's color
        self.color = input("Enter new vehicle color: ")

    def set_make(self): # Prompt user to update the vehicle's make
        self.make = input("Enter new vehicle make: ")

    def set_model(self): # Prompt user to update the vehicle's model
        self.model = input("Enter new vehicle model: ")

    def set_kilometers_per_kilowatt_hour(self):
        while True:
            try:
                km_per_kWh = float(input("Enter new vehicle efficiency (km/kWh): "))
                if km_per_kWh > 0:
                    self.kilometers_per_kilowatt_hour = km_per_kWh
                    break
                else:
                    print("Efficiency must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def set_max_kilowatt_hours(self):
        while True: # Loop until the user provides a valid max battery capacity
            try:
                kWh = float(input("Enter new maximum battery capacity (kWh): "))
                if kWh > 0:
                    self.max_kilowatt_hours = kWh
                    # Ensure current charge does not exceed new max capacity
                    if self.current_kilowatt_hours > self.max_kilowatt_hours:
                        self.current_kilowatt_hours = self.max_kilowatt_hours
                    break
                else:
                    print("Maximum Capacity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def set_current_kilowatt_hours(self):
        while True: # Loop until the user provides a valid current battery charge
            try:
                current_kWh = float(input("Enter new current battery charge (kWh): "))
                if 0 <= current_kWh <= self.max_kilowatt_hours:
                    self.current_kilowatt_hours = current_kWh
                    break
                else:
                    print(f"Battery charge must be between 0 and {self.max_kilowatt_hours} kWh.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def charge(self):# Calculate the available charging capacity
        available_charge = self.max_kilowatt_hours - self.current_kilowatt_hours
        print(f"Available charging capacity: {available_charge} kWh")

        while True: # Loop until the user provides a valid charge amount
            try:
                requested_charge = float(input("Enter amount to charge (kWh): "))
                if 0 <= requested_charge <= available_charge:
                    self.current_kilowatt_hours += requested_charge
                    print(f"Vehicle charged!\nCurrent battery level: {self.current_kilowatt_hours} kWh")
                    break
                else:
                    print(f"Cannot exceed max capacity. Max charge possible: {available_charge} kWh.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def drive(self): # Calculate the maximum possible driving distance
        available_distance = self.kilometers_per_kilowatt_hour * self.current_kilowatt_hours
        print(f"Maximum possible distance: {available_distance:.2f} km")

        while True: # Loop until the user provides a valid driving distance
            try:
                requested_distance = float(input("Enter distance to drive (km): "))
                energy_required = requested_distance / self.kilometers_per_kilowatt_hour
                # Check if there is enough charge for the requested distance
                if energy_required <= self.current_kilowatt_hours:
                    self.current_kilowatt_hours -= energy_required
                    print(f"Drive successful!\nRemaining battery: {self.current_kilowatt_hours:.2f} kWh")
                    break
                else:
                    print("Insufficient charge to cover the requested distance.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

ev = ElectricVehicle()

def main(): # Function to initialize ElectricVehicle class based on user input
    print(f"Welcome to Electric Vehicle!\nWould you like to use the default Electric Vehicle or input your own Electric "
          f"Vehicle?")

    while True:
        initial = int(input("1) Default\n2) Custom\nPlease choose 1 or 2:"))

        if initial == 1:
            print("\nUsing default Electric Vehicle!")
            print(ev.get_vehicle_info())
            break

        elif initial == 2:
            print("\nCreating a custom Electric Vehicle!")
            ev.set_color()
            ev.set_make()
            ev.set_model()
            ev.set_kilometers_per_kilowatt_hour()
            ev.set_max_kilowatt_hours()
            ev.set_current_kilowatt_hours()
            print("\nCustom Electric Vehicle Created!\n")
            print(ev.get_vehicle_info())
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    while True:
        print('\nWould you like to:\n1) Drive\n2) Charge\n3) Exit')
        user_input = input("Choose an option: ")

        if user_input == "1":
            ev.drive()
        elif user_input == "2":
            ev.charge()
        elif user_input == "3":
            print("Thank you for using the Electric Vehicle! Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

main()
# Function to convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371


# Function to convert miles to kilometers
def miles_to_km(miles):
    return miles / 0.621371


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Function to display menu and handle user input
def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Choose a conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} kilometers is equal to {km_to_miles(km)} miles.")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles is equal to {miles_to_km(miles)} kilometers.")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F.")
    elif choice == '4':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C.")
    else:
        print("Invalid choice! Please select a valid option.")


# Run the unit converter
unit_converter()

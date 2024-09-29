# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Factor for converting Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        elif unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()



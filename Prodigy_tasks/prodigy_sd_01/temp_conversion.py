def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")

    while True:
        try:
            temperature = float(input("Enter the temperature value: "))
            original_unit = input("Enter the original temperature unit (C, F, K): ").strip().upper()

            if original_unit == 'C':
                celsius = temperature
                fahrenheit = celsius_to_fahrenheit(celsius)
                kelvin = celsius_to_kelvin(celsius)
                print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit and {kelvin:.2f} Kelvin")

            elif original_unit == 'F':
                fahrenheit = temperature
                celsius = fahrenheit_to_celsius(fahrenheit)
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius and {kelvin:.2f} Kelvin")

            elif original_unit == 'K':
                kelvin = temperature
                celsius = kelvin_to_celsius(kelvin)
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                print(f"{kelvin} Kelvin is equal to {celsius:.2f} Celsius and {fahrenheit:.2f} Fahrenheit")

            else:
                print("Invalid input. Please enter C, F, or K.")
                continue

            another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
            if another_conversion != 'yes':
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()

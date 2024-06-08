#1 
#Task 1: User Input and Error Handling

def get_fahrenheit_temperature():
    while True:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            return fahrenheit
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

fahrenheit_temp = get_fahrenheit_temperature()

#Task 2: Temperature Conversion

def fahrenheit_to_celsius(fahreinheit):
    try:
        celsius = (fahreinheit - 32) * 5 / 9
        return celsius
    except ZeroDivisionError:
        print("Error: Cannot do division by zero for temperature conversion.")
        return None


#Task 3: User Experience
def main():
    
    
    try:
        fahrenheit_temp = get_fahrenheit_temperature()
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)

        if celsius_temp is not None:
            print(f"{fahrenheit_temp:.2f}f is approximately {celsius_temp: .2f}C.")
        else:
            print("Temperature conversion failed. Please try again.")
    finally:
        print("Thank your for using the weather forecast application.")
    
if __name__== "__main__":
    main()


#2. The Recipe Ratio Adjuster
#Task 1: Start

def get_servings_input(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Please enter a positive number of servings.")
            else:
                return servings
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

#Task2: Quantity Calculation

def adjustment_factor_cal(original_servings, desired_servings):
    try:
        return desired_servings / original_servings
    except ZeroDivisionError:
        print("Error: Original servings must be greater than zero.")
        return None
    
def main():
    try:
        original_servings = get_servings_input("Enter the original servings:")
        desired_servings = get_servings_input("Enter the desired servings:")

        adjustment_factor = adjustment_factor_cal(original_servings, desired_servings)

        if adjustment_factor is not None:
            print(f"Adjustment factor: {adjustment_factor: .2f}")
    finally:
        print("Enjoy your cooking!")

if __name__ == "__main__":
    main()

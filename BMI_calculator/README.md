# BMI Calculator

This is a simple BMI (Body Mass Index) calculator written in Python. It prompts the user to input their age, weight, and height, calculates their BMI, and then prints out a message based on the BMI value.

## Usage

1. Clone the repository or download the Python script.
2. Run the script using a Python interpreter.
3. Follow the prompts to enter your age, weight, and height.
4. The program will calculate your BMI and provide feedback on your weight status.

## Requirements

- Python 3.x

## How it works

The program first asks for the user's age, weight, and height. If the age is less than 18, it prints a message indicating that the BMI cannot be calculated. Otherwise, it calculates the BMI using the formula: weight / (height * height). Based on the calculated BMI value, the program prints a message indicating the user's weight status.

## Error Handling

The program uses exception handling to catch any errors that may occur during input conversion. If the user enters an invalid value (e.g., non-numeric input), the program displays a message asking the user to try again.

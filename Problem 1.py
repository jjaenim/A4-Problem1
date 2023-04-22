# Joshua Adrian O. Daet
# BSCpE 1-4
# Assignment 4 - Problem 1

# Open the input file for reading
with open("C:/assignments_oop/A4-Problem1/numbers.txt", "r") as input:
    numbers = input.read().split() # Read the numbers and split them into a list

even_numbers = [] # List to store even numbers
odd_numbers = []  # List to store odd numbers

# Iterate through the numbers and categorize them as even or odd
for number in numbers:
    number = int(number) # Convert the number from string to integer
    if number % 2 == 0:
        even_numbers.append(number) # Add even numbers to the even_numbers list
    else:
        odd_numbers.append(number) # Add odd numbers to the odd_numbers list

# Create even.txt and write even numbers to it
with open("even.txt", "w") as file:
    for number in even_numbers:
        file.write(str(number) + "\n") # Write each even number to a new line

# Create odd.txt and write odd numbers to it
with open("odd.txt", "w") as file:
    for number in odd_numbers:
        file.write(str(number) + "\n") # Write each odd number to a new line

print("Even and odd numbers are separated successfully and written to even.txt and odd.txt.")
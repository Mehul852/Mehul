# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 11:01:15 2024

@author: RAHUL KUMAR
"""

# Calculator
import math
# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Function to calculate square root of a number
def square_root(num):
    return math.sqrt(num)

# Main program
print("Welcome to the Calculator!")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Thank you for using the Calculator!")
        break

    if choice == '5':
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")
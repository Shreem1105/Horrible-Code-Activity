# Name: Harsh Makadia
# Assignment: Horrible Code Activity

import random  # YAGNI Violation: We import a module that never use

# Global variable are bad practice, but we are doing it
r = 0

def do_everything():
    global r  # Modifying global state inside a func

    # Useless comment
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Clean Code Violation: non descriptive variable names (c, x, y, r)
    c = input("Choose an operation (1-4): ")

    # DRY & SRP Violation: asking for input and doing math inside every single if statement
    if c == "1":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        r = x + y
        print("Result:", r)
    elif c == "2":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        r = x - y
        print("Result:", r)
    elif c == "3":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        r = x * y
        print("Result:", r)
    elif c == "4":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if y == 0:
            print("Cannot divide by zero")
        else:
            r = x / y
            print("Result:", r)
    else:
        print("Invalid choice")

# Run the code
do_everything()
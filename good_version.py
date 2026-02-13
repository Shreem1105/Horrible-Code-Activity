def add_numbers(first_number, second_number):
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    return first_number - second_number


def multiply_numbers(first_number, second_number):
    return first_number * second_number


def divide_numbers(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero"
    return first_number / second_number


def get_user_choice():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Choose an operation (1-4): ")


def main():
    choice = get_user_choice()

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    if choice == "1":
        result = add_numbers(first_number, second_number)
    elif choice == "2":
        result = subtract_numbers(first_number, second_number)
    elif choice == "3":
        result = multiply_numbers(first_number, second_number)
    elif choice == "4":
        result = divide_numbers(first_number, second_number)
    else:
        result = "Invalid choice"

    print("Result:", result)


main()

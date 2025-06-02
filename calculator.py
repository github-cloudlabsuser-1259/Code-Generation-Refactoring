# Create a basic calculator that can add, subtract, multiply, and divide two numbers.
def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y
def divide(x, y):
    """Return the quotient of x and y. Raises ValueError if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator(x, y, operation):
    """Perform the specified operation on x and y."""
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")

# Add functionality to ask user for input at the start of the program. 
# Ask the user whether they want to perform another calculation after each operation or exit. Give the user
# also the option to reuse the previous result in the next calculation.
def main():
    """Main function to run the calculator."""
    result = None
    while True:
        if result is not None:
            print(f"Previous result: {result}")
            use_previous = input("Do you want to use the previous result? (yes/no): ").strip().lower()
            if use_previous == 'yes':
                x = result
            else:
                x = float(input("Enter the first number: "))
        else:
            x = float(input("Enter the first number: "))
        
        y = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        
        try:
            result = calculator(x, y, operation)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)
        
        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            break
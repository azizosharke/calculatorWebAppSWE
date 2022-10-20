from sys import exit

precedence = {')': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# Function to check if a given character is a number.
# returns true/false.

def is_number(token):
    return str(token).replace('.', '').isdigit()


# Function to check if a given character is an operator.
# returns true/false.

def is_operator(token):
    return token in ['+', '-', '*', '/', '^', '(', ')']

def operation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("DIVISION BY 0 ERROR.")
            exit()
    elif operator == "^":
        return num1 ** num2

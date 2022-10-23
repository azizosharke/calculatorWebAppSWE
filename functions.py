from sys import exit

pre = {')': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# Function to check if a given character is a number.
# returns true/false.
def is_number(token):
    return str(token).replace('.', '').isdigit()

# Function to check if a given character is an operator.
# returns true/false.
def is_operator(token):
    return token in ['+', '-', '*', '/', '^', '(', ')']

# Function to check the operation and division by 0 .
# returns the results .
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

# Function to solve a mathematical equation
# Supports (), +, -, *, /, ^, and floating point numbers.
def calculator(equation: object) -> object:
    list = list_conversion(equation)
    for input in list:
        if is_number(input) or is_operator(input):
            continue
        print('Invalid token: ' + input)
        exit()
    return floating_numbers(string_conversion(equation))  

# Function to solve the expression in a list . Takes a list form and outputs a floating point number.
def floating_numbers(stringInput):
    global m, n
    list = []
    for number in stringInput:
        if not is_number(number):
            try:
                n = list.pop()
                m = list.pop()
            except IndexError:
                print("Invalid expression ! ")
                exit()
            list.append(operation(m, number, n))
        else:
            list.append(number)
    return list.pop()

# Function that converts a string containing a mathematical expression into a list in Reverse Polish Notation

def string_conversion(calc):
    expression = list_conversion(calc)
    result = []
    list = []
    for input in expression:
        if not is_number(input):
            if input == '(':
                list.insert(0, input)
            elif input == ')' and list:
                while list[0] != '(' and list:
                    result.append(list[0])
                    del list[0]
                if list and list[0] == '(':
                    pass
                else:
                    print("Invalid formatting of parentheses in expression.")
                    exit()
                del list[0]
            else:
                if not list:
                    pass
                else:
                    while (list and
                           (input != '^' and pre.get(input) <= pre.get(list[0])) or
                           (input == '^' and pre.get(input) < pre.get(list[0]))):
                        result.append(list[0])
                        del list[0]
                list.insert(0, input)
        else:
            result.append(input)
    while list:
        result.append(list[0])
        del list[0]
    return result

# Function to convert a string expression into a list

def list_conversion(s):
    empty_list = []
    i = 0
    while i != len(s):
        if is_number(s[i]):
            temp = s[i]
            while True:
                if i + 1 >= len(s):
                    temp = float(temp)
                    empty_list.append(temp)
                    break
                elif not (not is_number(s[i + 1]) and not (s[i + 1] == '.')):
                    temp += s[i + 1]  # | |
                    i += 1
                    continue
                temp = float(temp)
                empty_list.append(temp)
                break
        elif s[i] != ' ':
            empty_list.append(s[i])
        i += 1
    return empty_list

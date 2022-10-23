from utility import *


# Function to solve a mathematical equation
# Supports (), +, -, *, /, ^, and floating point numbers.
def calculator(equation: object) -> object:
    list = convert_to_list(equation)
    if type(list) == str:
        return list

    validation_result = validate_expression(list)
    if validation_result is not None:
        return validation_result
    else:
        result = evaluate(list)
        if type(result) == int or type(result) == float:
            return round(result, 3)
        return "Error: Complex Result"


# Function to convert a string expression into a list
def convert_to_list(input_to_calc: str):
    last_num = False
    # if true, next operator will be applied to number (for negation)
    next_unary = True
    negate = False
    floating = 0    # if number floating (ie not 0), divide char by 10^floating and add to last index
    expr = []
    for char in input_to_calc:
        if is_number(char):
            if floating != 0:
                if char == ".":
                    return "Error: number has two decimal points"
                if negate:
                    # convert string to number, subtract from end of number in list
                    expr[-1] = expr[-1] - ((ord(char) - 48) / 10 ** floating)
                else:
                    # convert string to number, add onto end of number in list
                    expr[-1] = expr[-1] + ((ord(char) - 48) / 10 ** floating)
                floating += 1
            elif last_num:
                if negate:
                    # convert string to number, subtract from end of number in list
                    expr[-1] = expr[-1] * 10 - (ord(char) - 48)
                else:
                    # convert string to number, add onto end of number in list
                    expr[-1] = expr[-1] * 10 + (ord(char) - 48)
            else:
                last_num = True
                if negate:
                    expr.append((ord(char) - 48) * -1)
                else:
                    # convert from string to number and add to list
                    expr.append(ord(char) - 48)

            # if operator follows number, it is not unary
            next_unary = False
        elif char == " ":
            last_num = False
            floating = False
        elif char == "-" and next_unary:
            negate = not negate
            floating = 0
        elif char == ")":
            expr.append(char)
            last_num = False
            negate = False
            floating = 0
        elif char == '.':
            if last_num == "":
                return "Error: must be a number before decimal point"
            if floating != 0:
                return "Error: number has two decimal points"
            floating += 1
        else:
            expr.append(char)
            last_num = False
            negate = False
            next_unary = True
            floating = 0

    return expr


def validate_expression(expression):
    if is_operator(expression[0]):
        return "Error: starts with operator"
    if is_operator(expression[-1]):
        return "Error: ends with operator"

    last_op = " "
    last_num = ""
    last_bracket = ""
    brackets = 0
    for i in expression:
        if type(i) == int or type(i) == float:
            if last_num != "":
                return "Error: two numbers in a row: " + last_num + " and " + str(i)
            if last_bracket == ")":
                return "Error: operator needed after right bracket"
            last_op = ""
            last_num = str(i)
            last_bracket = ""
        elif is_operator(i):
            if last_op != "":
                return "Error: two operators in a row: " + last_op + " and " + i
            if last_bracket == "(":
                return "Error: operator after left bracket"
            last_op = i
            last_num = ""
            last_bracket = ""
        elif i == "(":
            if last_op == "":
                return "Error: operator needed before left bracket"
            brackets += 1
            last_op = ""
            last_num = ""
            last_bracket = "("
        elif i == ")":
            if last_op != "":
                return "Error: operator before right bracket"
            brackets -= 1
            last_op = ""
            last_num = ""
            last_bracket = ")"
        else:
            return "Error: unrecognised character: " + str(i)

    if brackets > 0:
        return "Error: open left bracket"
    if brackets < 0:
        return "Error: open right bracket"
    return None


def perform_operation(val_stack, op_stack):
    val2 = val_stack.pop()
    val1 = val_stack.pop()
    op = op_stack.pop()
    res = operation(val1, op, val2)
    if type(res) == str:
        return res
    val_stack.append(res)
    return None


def evaluate(expr):
    val_stack = []
    op_stack = []
    for token in expr:
        if type(token) == int or type(token) == float:
            val_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while len(op_stack) != 0 and op_stack[-1] != "(":
                err = perform_operation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.pop()  # discard "("
        else:
            while len(op_stack) != 0 and op_stack[-1] != "(" and get_precedence(op_stack[-1]) >= get_precedence(token):
                err = perform_operation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.append(token)

    while len(op_stack) != 0:
        err = perform_operation(val_stack, op_stack)
        if err is not None:
            return err
    return val_stack.pop()

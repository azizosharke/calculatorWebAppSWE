from sys import exit

precedence = {')': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def is_number(token):
    return str(token).replace('.', '').isdigit()


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

    def floating_numbers(stringInput):
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




from evaluation import calculator


if __name__ == "__main__":
    while True:
        expression = input("Enter your Expression Here: ")
        if expression == "quit":
            break
        result = calculator(expression)
        if type(result) == str:
            print(result)
        else:
            print(f'Result: {result}')

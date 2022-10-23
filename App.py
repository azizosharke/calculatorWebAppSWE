from functions import *


if __name__ == "__main__":
    running = True
    while running:
        result = calculator(input("Enter your Expression Here: "))
        if result == "quit":
            running = False
        elif type(result) == str:
            print(result)
        else:
            print(f'Result: {result}')

import random

def get_random_between_1_10()-> int :
    """Return a random integer between 1 and 10 (inclusive)."""
    return random.randint(1, 10)

def get_random_operation()-> str:
    """Return a random operation symbol: one of '+', '-', '*', '%'"""
    return random.choice(['+', '-', '*', '/'])


def calc_result(num1, operation, num2)-> int:
    """Calculate and return the result of: num1 oper num2

    Supported operations: +, -, *, %

    Example:
        calc_result(7, '*', 3) -> 21
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2


num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")
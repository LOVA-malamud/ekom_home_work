import random

def get_luck_number(amount : int) -> tuple[int]:
    luck_list = []

    for i in range(amount):
        luck_list.append(random.randint(1,100))
    return tuple(luck_list)

def input_until_lucky(lucky_numbers : int) -> int:
    attempts : int = 0
    guess_correct = False

    print(f"you need you to choose one of {len(lucky_numbers)} lucky numbers")
    while not guess_correct:
        user_guess = input('enter your guess: ')
        try:
            guess = int(user_guess)
            attempts += 1
            if guess in lucky_numbers:
                print(f'your guess {user_guess} is corrct!')
                guess_correct = True
            else:
                print(f'your guess {user_guess} is wrong!')
        except ValueError:
            print(f'your guess "{user_guess}" is invalid !!! plz enter a number (this guess didnt count as attempt)')
    return attempts


secret_number = get_luck_number(40)
total_tries = input_until_lucky(secret_number)
print(f'it took {total_tries} tries')
def safe_code(secret_code: list) -> bool:
    index = 0
    
    while index < len(secret_code):
        user_input = input(f'Enter number {index + 1}: ')
        
        try:
            user_number = int(user_input)
        except ValueError:
            print("Please enter a valid number!")
            index = 0
            continue
        
        if user_number == secret_code[index]:
            print("Correct!")
            index += 1
        else:
            print("Wrong! reset the code.")
            index = 0
    
    print("Safe opened!")
    return True

secret_code = [77, 12, 43, 100, 51]
safe_code(secret_code)



time_input: int = int(input(' how long did it take you to receive your meal? '))
worth_input: int = int(input('how much did it cost? '))
if time_input < 15:
    is_quick_service: bool = True
else:
    is_quick_service: bool = False
if worth_input > 100:
    is_expensive: bool = True
else:
    is_expensive: bool = False
if is_quick_service and not is_expensive == True:
    print('recommended')
else:
    print('not recommended')

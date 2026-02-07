user_input: int = int(input('in a scale of 1 to 10, rate the volume'))
match user_input:
    case 1:
        print('very quiet')
    case 2:
        print('quiet')
    case 3 | 4:
        print('low')
    case 5:
        print('medium')
    case 6:
        print('medium high')
    case 7:
        print('loud')
    case 8:
        print('very loud')
    case 9 | 10 :
        print('max volume')
    case _:
        print('invalid volume')


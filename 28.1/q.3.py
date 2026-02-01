player_num: int = 0
player_over_16: int = 0
while player_num < 10:
    player_age: int = int(input("Enter player age: "))
    if player_age < 12:
        print("Player is too young")
        continue
    elif player_age > 18:
        print("Player is too old")
        break
    else:
        print('Player is added')
        player_num += 1
        if player_age > 16:
            player_over_16 += 1

print(f'Number of players: {player_num}')
print(f'Number of players over 16: {player_over_16}')


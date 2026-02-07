
import random
player_score: int = 0
computer_score: int = 0
# choose 10 random cards
while True:
    suit_player: int = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_player: int = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    suit_computer= random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_computer = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print("Your card is:", card_player, suit_player)
    print("Computer card is:", card_computer, suit_computer)

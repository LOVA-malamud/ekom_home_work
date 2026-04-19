import random

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50

print("=== SLOT MACHINE === \n")

def spin_slots():
    """Return 3 random symbols and their indexes"""
    return [random.choice(range(len(symbols))) for _ in range(3)]

def calculate_winnings(bet, spin_result):
    """Calculate winnings based on spin result"""
    symbol_counts = {}
    for idx in spin_result:
        symbol_counts[idx] = symbol_counts.get(idx, 0) + 1
    
    # Check for 3 of a kind
    for symbol_idx, count in symbol_counts.items():
        if count == 3:
            return bet * 777 * rate[symbol_idx]
    
    # Check for 2 of a kind
    for symbol_idx, count in symbol_counts.items():
        if count == 2:
            return bet * rate[symbol_idx]
    
    # All different - lose bet
    return 0

def display_spin(spin_result):
    """Display the spin result with symbols"""
    spin_symbols = [symbols[idx] for idx in spin_result]
    return " ".join(spin_symbols)

# Main game loop
while money > 0:
    print(f"\nCurrent money: ${money}")
    
    # Get bet amount
    while True:
        bet_input = input("Enter your bet (or 'quit' to exit): ")
        
        if bet_input.lower() == 'quit':
            print("Thanks for playing!")
            exit()
        
        try:
            bet = int(bet_input)
            if 1 <= bet <= money:
                break
            else:
                print(f"Bet must be between 1 and {money}")
        except ValueError:
            print("Please enter a valid number")
    
    # Spin the slots
    spin_result = spin_slots()
    spin_display = display_spin(spin_result)
    print(f"\nSpin result: {spin_display}")
    
    # Calculate and display winnings
    winnings = calculate_winnings(bet, spin_result)
    
    if winnings > 0:
        money += winnings
        print(f"You won ${winnings}!")
    else:
        money -= bet
        print(f"You lost ${bet}")

print("\nGame Over! You're out of money!")
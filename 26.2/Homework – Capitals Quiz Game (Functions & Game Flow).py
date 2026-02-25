import random

QUESTIONS = [
    "What is the capital of France? (1) Paris (2) Lyon (3) Marseille (4) Nice",
    "What is the capital of Italy? (1) Milan (2) Venice (3) Rome (4) Naples",
    "What is the capital of Spain? (1) Barcelona (2) Seville (3) Madrid (4) Valencia",
    "What is the capital of Portugal? (1) Porto (2) Lisbon (3) Faro (4) Braga",
    "What is the capital of Greece? (1) Thessaloniki (2) Athens (3) Patras (4) Heraklion",
    "What is the capital of Netherlands? (1) Rotterdam (2) Utrecht (3) Eindhoven (4) Amsterdam",
    "What is the capital of Belgium? (1) Antwerp (2) Bruges (3) Brussels (4) Ghent",
    "What is the capital of Switzerland? (1) Zurich (2) Geneva (3) Basel (4) Bern",
    "What is the capital of Austria? (1) Salzburg (2) Vienna (3) Graz (4) Innsbruck",
    "What is the capital of Canada? (1) Toronto (2) Vancouver (3) Ottawa (4) Montreal",
    "What is the capital of Brazil? (1) Rio de Janeiro (2) São Paulo (3) Brasília (4) Salvador",
    "What is the capital of Japan? (1) Osaka (2) Tokyo (3) Kyoto (4) Hiroshima",
    "What is the capital of Australia? (1) Sydney (2) Melbourne (3) Canberra (4) Perth",
    "What is the capital of India? (1) Mumbai (2) New Delhi (3) Bangalore (4) Chennai",
    "What is the capital of Egypt? (1) Alexandria (2) Giza (3) Cairo (4) Luxor",
    "What is the capital of Mexico? (1) Guadalajara (2) Monterrey (3) Cancún (4) Mexico City",
    "What is the capital of Argentina? (1) Córdoba (2) Rosario (3) Mendoza (4) Buenos Aires",
    "What is the capital of South Korea? (1) Busan (2) Incheon (3) Seoul (4) Daegu",
    "What is the capital of Sweden? (1) Gothenburg (2) Malmö (3) Uppsala (4) Stockholm",
    "What is the capital of Norway? (1) Bergen (2) Oslo (3) Trondheim (4) Stavanger"
]

ANSWERS = [1, 3, 3, 2, 2, 4, 3, 4, 2, 3, 3, 2, 3, 2, 3, 4, 4, 3, 4, 2]

def get_random_question():
    """Return a random question index."""
    return random.randint(0, len(QUESTIONS) - 1)

def display_question(index):
    """Display the question at the given index."""
    print(QUESTIONS[index])

def get_user_choice():
    """Get and validate user's choice (1-4)."""
    while True:
        choice_str = input("Enter your choice (1-4): ")
        if choice_str.isdigit():
            choice = int(choice_str)
            if 1 <= choice <= 4:
                return choice
        print("Invalid input. Please enter a number between 1 and 4.")

def user_answer_is_correct(index, user_choice):
    """Check if user's answer is correct."""
    return user_choice == ANSWERS[index]

def remove_question(index):
    """Remove question and answer at the given index."""
    QUESTIONS.pop(index)
    ANSWERS.pop(index)

def check_if_score_is_5(score):
    """Check if score reached 5 (winning condition)."""
    return score == 5

def check_if_miss_is_3(miss):
    """Check if misses reached 3 (losing condition)."""
    return miss == 3

def get_correct_city_name(index):
    """Extract the correct city name from the question string."""
    correct_num = ANSWERS[index]
    parts = QUESTIONS[index].split(f"({correct_num}) ")
    right_side = parts[1]
    if "(" in right_side:
        city = right_side.split(" (")[0]
    else:
        city = right_side
    return city.strip()


    """Main game loop."""
score = 0
miss = 0

while True:
        question_index = get_random_question()
        display_question(question_index)

        user_choice = get_user_choice()

        if user_answer_is_correct(question_index, user_choice):
            score += 1
            print("You are correct")
        else:
            miss += 1
            correct_city = get_correct_city_name(question_index)
            print(f"You are wrong! The correct city was: {correct_city}")

        remove_question(question_index)

        if check_if_score_is_5(score):
            print("WINNER !!!")
            break

        if check_if_miss_is_3(miss):
            print("YOU LOST !!!")
            break



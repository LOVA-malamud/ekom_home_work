grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

def get_average_grade(grades: dict) -> float:
    total = sum(grades.values())
    return total / len(grades)
print(get_average_grade(grades))

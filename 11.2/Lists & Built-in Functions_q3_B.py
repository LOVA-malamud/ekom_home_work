words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]
print(all(word.isupper() for word in words))
print(any(len(word) == 5 for word in words))

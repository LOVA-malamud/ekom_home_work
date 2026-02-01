num_streak: int = 0
highest_num: int = 0
while num_streak < 3:
    num: int = int(input("Enter number: "))
    if num > highest_num:
        highest_num = num
        num_streak += 1
    elif num <= highest_num:
        num_streak = 1
        highest_num = num
print(f"your highest num is {highest_num}")
print(f"your streak is {num_streak}")
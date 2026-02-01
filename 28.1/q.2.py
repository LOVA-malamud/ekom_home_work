i: int = 0
while True:
    lower: int = int(input("Enter lower limit: "))
    higher: int = int(input("Enter higher limit: "))
    if higher <= lower:
        continue
    else:
        break
for i in range(lower, higher + 1):
    print(i)
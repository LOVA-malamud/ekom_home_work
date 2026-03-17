list = [4, -2, 0, 7, -5, 3]

def group_numbers(nums: list) -> dict:
    result = {"positive": [], "negative": [], "zero": []}

    for num in nums:
        if num > 0:
            result["positive"].append(num)
        elif num < 0:
            result["negative"].append(num)
        else:
            result["zero"].append(num)
    return result

print(group_numbers(list))

def get_statistics(numbers):
    max_numbers = max(numbers)
    min_numbers = min(numbers)
    sum_numbers = sum(numbers)
    len_numbers = len(numbers)
    avg_numbers  = sum_numbers / len_numbers
    dict_numbers = {
        'sum': sum_numbers,
        'avg': avg_numbers,
        'min': min_numbers,
        'max': max_numbers,
        'length': len_numbers
    }
    return dict_numbers



numbers = [4, 8, 2, 10, 6]
result = get_statistics(numbers)
print(result)
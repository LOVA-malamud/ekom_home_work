def biggest_number(nums: list,n: int) -> int:
    nums_set = set(nums)
    sorted_nums = sorted(nums_set, reverse=True)
    return sorted_nums[n]

print(biggest_number([88, 100, 90, 95, 95, 97, 97, 99, 97, 99], 3))

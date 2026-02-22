import statistics

numbers = [10, 20, 30, 20, 40, 50]
print(f'the number 20 count ,{numbers.count(20)} time')
print(f'the index of number 30 is ,{numbers.index(30)}')
numbers.append(99)
print(numbers)
numbers.insert(2, 15)
print(numbers)
numbers.remove(20)
print(numbers)
print(f'number remove from index 3 is , {numbers.pop(3)}')
print(f'the highest number is , {max(numbers)}')
print(f'the lowest number is , {min(numbers)}')
print(f'the sum of numbers is , {sum(numbers)}')
print(f' the average of all numbers is {statistics.mean(numbers)}')
print(f' there is {len(numbers)} numbers in the list')

def basic_math_list(a:int, b:int):
    """
    this function returns a list of basic math operations
    :param a: first num
    :param b: sec num
    :return: list of basic math operations
    """
    return [a + b, a - b, a / b, a * b]
result = basic_math_list(10, 2)
print(result)

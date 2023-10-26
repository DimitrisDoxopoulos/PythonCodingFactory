def my_add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the results

    Args:
    a (int) -- the first number to add
    b (int) -- the second number to add

    Returns
    The sum of a and b
    """
    return a + b

print('Annotations', my_add.__annotations__)
print('Doc:', my_add.__doc__)
print('10 + 20 = ', my_add(10, 20))

help(my_add)
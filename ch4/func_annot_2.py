def my_add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers and returns the results

    Args:
    a (int, float) -- the first number to add
    b (int, float) -- the second number to add

    Returns
    (int, float) The sum of a and b
    """
    return a + b

print('Annotations', my_add.__annotations__)
print('Doc:', my_add.__doc__)
print('10 + 20 = ', my_add(10.4, 20))

help(my_add)
def my_add(a, b):
    """
    Adds two numbers and returns the results

    Args:
    a (int, float) -- the first number to add
    b (int, float) -- the second number to add

    Returns
    The sum of a and b
    """
    if not ((isinstance(a, int) or isinstance(a, float))
            and (isinstance(b, int) or isinstance(b, float))):
        return 0

    return a + b

def my_add_2(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return 0
    
    return a + b

print(my_add(10, 20))
print(my_add(5, 8.3))
print(my_add("Hello ", "Coding Factory"))

print(my_add_2(10, 20))
print(my_add_2(5, 8.3))
print(my_add_2("Hello ", "Coding Factory"))
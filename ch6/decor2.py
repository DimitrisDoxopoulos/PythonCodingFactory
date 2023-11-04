import time

def timer_decorator(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        # make my calculations
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}: took {end_time - start_time: .5f} seconds to run')
        return result
    return inner_function

def sum_function(n):
    return sum(range(n))

sum_f_2 = timer_decorator(sum_function)

print(sum_f_2(1000000))

@timer_decorator
def def_example(n):
    return sum(range(n))

print(def_example(2000000))

@timer_decorator
def def_example_2(s):
    return ''.join(reversed(s))

print(def_example_2("Coding Factory"))

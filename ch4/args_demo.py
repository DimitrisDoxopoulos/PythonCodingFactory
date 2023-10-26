# Varargs

def my_add(*args):
    # result = 0
    
    # for arg in args:
    #     result += arg
    # return result
    
    return sum(args)

def my_avg(*args):
    # sum = 0
    # for arg in args:
    #     sum += arg
    
    # return sum / len(args)
    return sum(args) / len(args)

ages = [27, 35, 42, 18, 20]
# print(my_avg(ages)) # This is a mistake because we need to unpack the age list
print(my_avg(*ages))

print(my_add())
print(my_add(1, 2, 3, 4, 5))
print(my_add(1, 2, 3, 4, 5, 6))
print(my_add(1, 2, 3, 4, 5, 6, 7))

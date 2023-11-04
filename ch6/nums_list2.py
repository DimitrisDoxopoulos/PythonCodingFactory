nums = [1, 2, 3, 4, 5]

num_to_find = 20

try:
    index = nums.index(num_to_find)
    print(f'index of {num_to_find} is {index}')
except ValueError as e:
    print(e)
    
num_to_find = 3
count = nums.count(3)

try:
    print(f'{num_to_find} is present in the list {count} time(s)')
except ValueError as e:
    print(e)

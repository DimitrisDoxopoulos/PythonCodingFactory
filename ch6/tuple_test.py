# tuple mutability test
my_tuple = (1, 2, [3, 'CF'], 'Hello')

print(my_tuple[1])

for item in my_tuple:
    print(id(item), ' : ', item)

my_tuple[2][0] = 200

print(my_tuple[1])

for item in my_tuple:
    print(id(item), ' : ', item)

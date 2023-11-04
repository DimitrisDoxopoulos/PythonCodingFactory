bag1 = {'A1', 'A2', 'A3', 'A4', 'BA1'}
bag2 = {'A1', 'A2', 'B3', 'B4', 'BB2'}

common_elements = bag1 & bag2

print('Common elements of bag1 and bag2 are: ', common_elements)

all_the_elements = bag1 | bag2
all_the_elements = bag1.union(bag2)
# Sets do not allow dublicates
print('All the elements: ', all_the_elements)

diff1 = bag1 - bag2
diff1 = bag1.difference(bag2)
print('The differences between bag1 and bag2: ', diff1)

diff2 = bag1 ^ bag2 # summetriki diafora
diff2 = bag1.symmetric_difference(bag2)
# All the elements except fromm the common ones
print('Symmetric differences between bag1 and bag2: ', diff2)

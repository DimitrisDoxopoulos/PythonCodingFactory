# Dictionaries Demo

products = {1: 'apples', 2: 'bananas'}

print(products)

# Insert
products[3] = 'oranges'
print(products)

# Update
products[3] = 'milk'
print(products)

# Delete
del products[1]
print(products)

for key in products.keys():
    print(key, products[key])

for value in products.values():
    print(value)

for key, value in products.items():
    print(key, ": ", value)